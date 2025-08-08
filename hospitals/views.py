from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Hospital, HospitalReview
from django.db.models import Avg

from doctors.models import Doctor

def home(request):
    return render(request, 'home.html')

def book_appointment(request):
    return render(request, 'home.html')
def hospital_list(request):
    selected_state = request.GET.get('state')
    selected_district = request.GET.get('district')
    selected_category = request.GET.get('category')
    hospitals = Hospital.objects.all()

    if selected_state:
        hospitals = hospitals.filter(state=selected_state)
    if selected_district:
        hospitals = hospitals.filter(district=selected_district)
    if selected_category:
        hospitals = hospitals.filter(category=selected_category)
    all_states = Hospital.objects.values_list('state', flat=True).distinct().order_by('state')
    all_districts = Hospital.objects.values_list('district', flat=True).distinct().order_by('district')
    all_categories = Hospital.objects.values_list('category', flat=True).distinct().order_by('category')

    context = {
        'hospitals': hospitals,
        'all_states': all_states,
        'all_districts': all_districts,
        'all_categories': all_categories,
        'selected_state': selected_state,
        'selected_district': selected_district,
        'selected_category': selected_category,

    }

    return render(request, 'hospital_list.html', context)


def hospital_details(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    
    # Handle review submission
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if user_name and rating:
            try:
                rating = int(rating)
                if 1 <= rating <= 5:
                    HospitalReview.objects.create(
                        hospital=hospital,
                        user=user_name,
                        rating=rating,
                        comment=comment or ''
                    )
                    messages.success(request, 'Your review has been submitted successfully!')
                else:
                    messages.error(request, 'Rating must be between 1 and 5.')
            except ValueError:
                messages.error(request, 'Invalid rating value.')
        else:
            messages.error(request, 'Please provide your name and rating.')
        
        return redirect('hospital_details', hospital_id=hospital_id)
    
    # Get all reviews for this hospital
    reviews = hospital.reviews.all()
    
    # Calculate average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating:
        avg_rating = round(avg_rating, 1)
    
    # Get review statistics
    total_reviews = reviews.count()
    rating_distribution = {}
    for i in range(1, 6):
        rating_distribution[i] = reviews.filter(rating=i).count()
    
    context = {
        'hospital': hospital,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'total_reviews': total_reviews,
        'rating_distribution': rating_distribution,
    }
    
    return render(request, 'hospital_detail.html', context)