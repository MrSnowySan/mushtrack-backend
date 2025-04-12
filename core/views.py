from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Batch
from django.contrib.auth.models import User
import json

# 👇 Render the dashboard without login requirement
def dashboard(request):
    return render(request, 'dashboard.html')

# 👇 Create a batch with hardcoded user (mushmaster)
@csrf_exempt
def create_batch(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            user = User.objects.get(username=data.get('username', 'mushmaster'))
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

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

# 👇 Get ALL batches regardless of user
@csrf_exempt
def get_batches(request):
    batches = Batch.objects.all()

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
        'harvests': []  # Placeholder for future harvest tracking
    } for b in batches]

    return JsonResponse(data, safe=False)
