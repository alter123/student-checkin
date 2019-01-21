
import os
import uuid
from itertools import chain

import pandas as pd
from django.core.files.storage import FileSystemStorage, default_storage
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SlotForm
from .models import Attendee, Document, Slots


def home(request):
    return render(request, 'home.html')


def checkin(request):

    branches = set()
    slot = Slots.objects.get(pk=1)
    qs = Attendee.objects.none()
    
    val = [ branches.add( getattr(slot, f'slot_{i+1}') ) 
     for i in range(9) if getattr(slot, f'filled_seats_{int(i/3)+1}') 
     < getattr(slot, f'total_seats_{int(i/3)+1}')  ]
    del val

    for branch in branches:
        qs |= Attendee.objects.filter(branch=branch, checkin=False)

    if request.is_ajax():
        query   = request.GET.get('query', None)+'/'
        results = Attendee.objects.filter(
            Q( name__contains = query.split('/')[0] )
          & Q( branch__contains = query.split('/')[1].strip() )
        ) & qs

        data, list = {}, []
        for attendee in results:
            student = {}
            student['name'] = attendee.name
            student['rollno'] = attendee.roll_no
            student['branch'] = attendee.branch
            student['pk'] = attendee.pk
            list.append(student)
        data['list'] = list

        return JsonResponse(data)
    return render(request, 'checkin.html')


def reserve(request):

    if request.is_ajax():
        slot = Slots.objects.get(pk=1)

        pk = request.GET.get('pk', None)
        student = Attendee.objects.get(pk=pk)

        for i in range(9):
            if ( getattr(slot, f'filled_seats_{int(i/3)+1}') < getattr(slot, f'total_seats_{int(i/3)+1}') ) and ( getattr(slot, f'slot_{i+1}') == student.branch ) : 
                setattr(slot, f'filled_seats_{int(i/3)+1}', 
                    getattr(slot, f'filled_seats_{int(i/3)+1}')+1 )
                student.seat_no = getattr(slot, f'filled_seats_{int(i/3)+1}')
                student.save()
                slot.save()
                break

        student.checkin = True
        student.checkin_time = timezone.now()
        student.save()
        return JsonResponse({'data': 'sucess!'})
    return JsonResponse({'data': 'Invalid Request'})


def checkins(request):

    attendee_list = Attendee.objects.filter(
        checkin=True).order_by('-checkin_time')
    if attendee_list:
        return render(request, 'tables/checkins.html', {'attendee_list': attendee_list})
    else:
        return render(request, 'tables/checkins.html', {'empty': ' '})


def branch_list(request, branch):

    attendee_list = Attendee.objects.filter( checkin=True, branch=branch ).order_by('-checkin_time')
    if attendee_list:
        return render(request, 'tables/branch-list.html', {'attendee_list': attendee_list})
    else:
        return render(request, 'tables/branch-list.html', {'empty': ' '})


def attendee_list(request):

    _attendee_list = Attendee.objects.all()
    if _attendee_list:
        return render(request, 'tables/checkins.html', {'attendee_list': _attendee_list})
    else:
        return render(request, 'tables/checkins.html', {'empty': ' '})

def upload_file(request):

    documents = Document.objects.all()
    if request.method == 'POST' and request.FILES['studentList']:
        studentList = request.FILES['studentList']
        branch = request.POST.get('branch')
        fs = FileSystemStorage()
        filename = fs.save(f'{str(uuid.uuid4())[:5]}.xlsx', studentList)
        fileurl = fs.url(filename)
        doc = Document(branch=branch, name=filename, document=fileurl)
        doc.save()

        return render(request, 'upload.html', {'message': 'File Sucessfully Uploaded',
                                             'document': documents})
    return render(request, 'upload.html', {'document': documents})


def delete_file(request, pk):

    if request.method == 'GET':
        doc = get_object_or_404(Document, pk=pk)
        doc.delete()
        return JsonResponse({'message': f'file {doc.name} has been deleted!'})
    else:
        return JsonResponse({'message': 'failed to process!'})


def populate(request, pk):
    """ Populates database from uploaded document """

    if request.method == 'GET':
        doc = get_object_or_404(Document, pk=pk)

        excel_file = open(os.getcwd()+str(doc.document), "rb")
        rows = pd.read_excel(excel_file, sheet_name=0, header=None, skiprows=1)
        for i in range(len(rows)):
            try:
                attendee = Attendee( name = rows[0][i], roll_no=rows[1][i], branch = doc.branch )
                attendee.save()
            except AttributeError:
                print('error while row: ', i)

        return JsonResponse({'message': f'file {doc.name} has been populated!'})
    else:
        return JsonResponse({'message': 'failed to process!'})
        

def manage(request):

    if request.is_ajax():
        req = request.GET.get('type')
        
        if req == 'checkout':
            queryset = Attendee.objects.all()
            for query in queryset:
                query.checkin = False
                query.save()
            return JsonResponse({ 'message': 'sucess' })
        
        elif req == 'delete':
            print('here')    
            Attendee.objects.all().delete()
            return JsonResponse({ 'message': 'sucess' })

        else:
            return JsonResponse({ 'message': 'Invalid request' })


def slot_form(request):

    slot = get_object_or_404(Slots, pk=1)

    if request.method == "POST":
        form = SlotForm(request.POST, instance=slot)

        if form.is_valid():
            form.save(commit=False)

            slot.total_seats_1 = form.cleaned_data['reserved'] + form.cleaned_data['total_seats_1']
            slot.total_seats_2 = slot.total_seats_1 + form.cleaned_data['total_seats_2']
            slot.total_seats_3 = slot.total_seats_2 + form.cleaned_data['total_seats_3']

            if form.cleaned_data['update_choice'] == '1':
                slot.filled_seats_1 = form.cleaned_data['reserved']
                slot.filled_seats_2 = slot.filled_seats_1 + form.cleaned_data['total_seats_1']
                slot.filled_seats_3 = slot.filled_seats_2 + form.cleaned_data['total_seats_2']

            slot.save()
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = SlotForm(
            initial={
                'slot_1': slot.slot_1,
                'slot_2': slot.slot_2,
                'slot_3': slot.slot_3,
                'slot_4': slot.slot_4,
                'slot_5': slot.slot_5,
                'slot_6': slot.slot_6,
                'slot_7': slot.slot_7,
                'slot_8': slot.slot_8,
                'slot_9': slot.slot_9,
                'total_seats_1': slot.total_seats_1 - slot.reserved,
                'total_seats_2': slot.total_seats_2 - slot.total_seats_1,
                'total_seats_3': slot.total_seats_3 - slot.total_seats_2,
                'filled_seats_1': slot.total_seats_1 - slot.filled_seats_1,
                'filled_seats_2': slot.total_seats_2 - slot.filled_seats_2,
                'filled_seats_3': slot.total_seats_3 - slot.filled_seats_3,
            }, instance=slot)

    return render(request, 'form.html', {'form': form})
