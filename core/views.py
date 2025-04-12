from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Batch
from django.contrib.auth.models import User

@csrf_exempt
def create_batch(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user = User.objects.get(username=data.get('username'))  # assume mushmaster for now

        batch = Batch.objects.create(
            user=user,
            batch_label=data['batchLabel'],
            variety=data['variety'],
            inoculation_date=data['inoculationDate'],
            num_bags=data['numBags'],
            contaminated_bags=data.get('contaminatedBags', 0),
            notes=data.get('notes', ''),
            stage='incubation'
        )

        return JsonResponse({'status': 'success', 'id': batch.id})
    
    return JsonResponse({'error': 'Invalid method'}, status=400)

from django.contrib.auth.decorators import login_required

@login_required
def get_batches(request):
    user = request.user  # logged-in user
    batches = Batch.objects.filter(user=user)

    data = [{
        'id': b.id,
        'batchLabel': b.batch_label,
        'variety': b.variety,
        'inoculationDate': str(b.inoculation_date),
        'numBags': b.num_bags,
        'contaminatedBags': b.contaminated_bags,
        'notes': b.notes,
        'stage': b.stage,
        'retirementDate': str(b.retirement_date) if b.retirement_date else None,
        'growRoomEntryDate': str(b.grow_room_entry_date) if b.grow_room_entry_date else None,
        'harvests': []  # You’ll expand this later when you track harvests
    } for b in batches]

    return JsonResponse(data, safe=False)
