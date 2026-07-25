from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse


def home(request):
    """Landing page view"""
    context = {
        'page_title': 'Home - American Red Cross Delivery',
        'hero_title': 'Fast & Reliable Delivery Services',
        'hero_subtitle': 'Delivering essentials to your doorstep with care and compassion',
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us - American Red Cross Delivery',
        'about_title': 'About Our Delivery Mission',
    }
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    services_list = [
        {
            'icon': '🚚',
            'title': 'Emergency Relief Delivery',
            'description': 'Swift delivery of emergency supplies and aid materials to affected communities.'
        },
        {
            'icon': '📦',
            'title': 'Blood Supply Transportation',
            'description': 'Temperature-controlled transport ensuring safe blood product delivery.'
        },
        {
            'icon': '🏥',
            'title': 'Medical Equipment Delivery',
            'description': 'Reliable delivery of medical equipment and healthcare supplies.'
        },
        {
            'icon': '🤝',
            'title': 'Disaster Relief Logistics',
            'description': 'Comprehensive disaster response and supply distribution services.'
        },
        {
            'icon': '🌍',
            'title': 'Community Support',
            'description': 'Local delivery support for community health initiatives and programs.'
        },
        {
            'icon': '⚡',
            'title': 'Express Delivery',
            'description': 'Same-day and next-day delivery options for urgent needs.'
        },
    ]
    context = {
        'page_title': 'Our Services - American Red Cross Delivery',
        'services': services_list,
    }
    return render(request, 'services.html', context)


def how_it_works(request):
    """How it works page"""
    steps = [
        {
            'step': '1',
            'title': 'Request a Delivery',
            'description': 'Submit your delivery request through our online platform or call our support team.'
        },
        {
            'step': '2',
            'title': 'Confirmation',
            'description': 'We confirm your order and prepare the items for dispatch with care.'
        },
        {
            'step': '3',
            'title': 'Track in Real-time',
            'description': 'Monitor your delivery in real-time with our advanced tracking system.'
        },
        {
            'step': '4',
            'title': 'Safe Delivery',
            'description': 'Your items arrive safely and on time with our trained delivery professionals.'
        },
    ]
    context = {
        'page_title': 'How It Works - American Red Cross Delivery',
        'steps': steps,
    }
    return render(request, 'how_it_works.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        # In a real app, you'd save this or send an email
        return JsonResponse({'status': 'success', 'message': 'Thank you for reaching out!'})
    
    context = {
        'page_title': 'Contact Us - American Red Cross Delivery',
    }
    return render(request, 'contact.html', context)


def faq(request):
    """FAQ page view"""
    faqs = [
        {
            'question': 'How quickly can you deliver?',
            'answer': 'We offer same-day delivery in most urban areas and next-day delivery for surrounding regions. Emergency deliveries are prioritized.'
        },
        {
            'question': 'What items can be delivered?',
            'answer': 'We deliver emergency supplies, medical equipment, blood products, relief materials, and other approved items based on our service offerings.'
        },
        {
            'question': 'Is tracking available?',
            'answer': 'Yes, all deliveries include real-time GPS tracking so you can monitor your shipment from pickup to delivery.'
        },
        {
            'question': 'What are your delivery rates?',
            'answer': 'Pricing depends on delivery distance, item type, and urgency. Contact our team for a custom quote.'
        },
        {
            'question': 'Do you deliver on weekends?',
            'answer': 'Yes, we offer weekend and holiday deliveries for emergency relief situations. Standard rates may vary.'
        },
        {
            'question': 'How can I schedule a delivery?',
            'answer': 'You can request a delivery online through our website, via phone, or through our mobile app. Our team will confirm availability.'
        },
        {
            'question': 'What if something is damaged?',
            'answer': 'All items are insured. Report damage within 24 hours with photos, and we\'ll process a claim immediately.'
        },
        {
            'question': 'Do you offer subscription services?',
            'answer': 'Yes, organizations can set up recurring delivery schedules with special pricing for regular shipments.'
        },
    ]
    context = {
        'page_title': 'FAQ - American Red Cross Delivery',
        'faqs': faqs,
    }
    return render(request, 'faq.html', context)


def blog(request):
    """Blog/News page view"""
    blog_posts = [
        {
            'id': 1,
            'title': 'Emergency Response: How Our Delivery Network Saved Lives',
            'date': 'July 20, 2024',
            'author': 'Sarah Johnson',
            'image': 'https://images.unsplash.com/photo-1517649763962-0c623066013b?w=900&h=600&fit=crop',
            'excerpt': 'During the recent natural disaster, our delivery team mobilized to deliver emergency supplies to over 5,000 families...',
            'category': 'News'
        },
        {
            'id': 2,
            'title': '5 Ways to Prepare for Emergency Situations',
            'date': 'July 15, 2024',
            'author': 'Michael Chen',
            'image': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=900&h=600&fit=crop',
            'excerpt': 'Being prepared is crucial during emergencies. Here are five essential steps you can take right now...',
            'category': 'Tips'
        },
        {
            'id': 3,
            'title': 'Introducing Our New Temperature-Controlled Delivery Fleet',
            'date': 'July 10, 2024',
            'author': 'Emily Rodriguez',
            'image': 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=900&h=600&fit=crop',
            'excerpt': 'We\'re excited to announce the addition of 50 new temperature-controlled vehicles to our fleet...',
            'category': 'Updates'
        },
        {
            'id': 4,
            'title': 'Community Impact: Blood Drive Success Records',
            'date': 'July 5, 2024',
            'author': 'David Martinez',
            'image': 'https://images.unsplash.com/photo-1489515217757-5fd1be406fef?w=900&h=600&fit=crop',
            'excerpt': 'Our July blood drives exceeded expectations with record-breaking participation across all regions...',
            'category': 'Impact'
        },
        {
            'id': 5,
            'title': 'Delivery Driver Spotlight: Meet Our Heroes',
            'date': 'June 28, 2024',
            'author': 'Lisa Thompson',
            'image': 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=900&h=600&fit=crop',
            'excerpt': 'Learn about the dedicated drivers who work tirelessly to ensure critical supplies reach those in need...',
            'category': 'Stories'
        },
        {
            'id': 6,
            'title': 'Sustainability in Delivery: Our Green Initiative',
            'date': 'June 20, 2024',
            'author': 'James Wilson',
            'image': 'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=900&h=600&fit=crop',
            'excerpt': 'We\'re committed to reducing our carbon footprint with electric vehicles and eco-friendly practices...',
            'category': 'Environment'
        },
    ]
    context = {
        'page_title': 'Blog & News - American Red Cross Delivery',
        'blog_posts': blog_posts,
    }
    return render(request, 'blog.html', context)

