from django.shortcuts import redirect, render

DEMO_ACCOUNTS = [
    {
        'email': 'cliente@lookby.cl',
        'password': '123456',
        'role': 'client',
        'name': 'Sofía Alarcón',
        'display_role': 'CLIENTE',
    },
    {
        'email': 'negocio@lookby.cl',
        'password': '123456',
        'role': 'business',
        'name': 'Atelier Doré',
        'display_role': 'NEGOCIO',
    },
    {
        'email': 'proveedor@lookby.cl',
        'password': '123456',
        'role': 'supplier',
        'name': 'Luna Supply',
        'display_role': 'PROVEEDOR',
    },
    {
        'email': 'admin@lookby.cl',
        'password': 'admin2026',
        'role': 'superadmin',
        'name': 'Valeria Ramos',
        'display_role': 'SUPERADMIN',
    },
]

CATEGORIES = [
    {'title': 'Facial', 'description': 'Tratamientos intensivos para luminosidad y rejuvenecimiento.'},
    {'title': 'Pestañas', 'description': 'Lifting, tinte y diseño con atención premium.'},
    {'title': 'Manicura', 'description': 'Detalle y precisión con tendencias de lujo.'},
    {'title': 'Spa', 'description': 'Relajación, bienestar y cuidado total para tu cuerpo.'},
]

SALONS = [
    {'name': 'Atelier Doré', 'location': 'Providencia', 'rating': '4.9', 'tag': 'VIP'},
    {'name': 'Luna Studio', 'location': 'Las Condes', 'rating': '4.8', 'tag': 'Top'},
    {'name': 'Aurelia Beauty', 'location': 'Ñuñoa', 'rating': '4.7', 'tag': 'Nuevo'},
]

PRODUCTS = [
    {'name': 'Serum Luminosa', 'category': 'Skincare', 'price': '$92.000'},
    {'name': 'Kit Repair', 'category': 'Tratamiento', 'price': '$135.000'},
    {'name': 'Glow Mist', 'category': 'Toners', 'price': '$69.000'},
    {'name': 'Radiance Oil', 'category': 'Aceites', 'price': '$118.000'},
]


def _get_session_user(request):
    return request.session.get('user')


def _login_user(request, user):
    request.session['user'] = {
        'name': user['name'],
        'email': user['email'],
        'role': user['role'],
        'display_role': user['display_role'],
    }


def _redirect_for_role(role):
    return {
        'client': 'client_dashboard',
        'business': 'business_dashboard',
        'supplier': 'supplier_dashboard',
        'superadmin': 'superadmin_dashboard',
    }.get(role, 'home')


def home(request):
    context = {
        'categories': CATEGORIES,
        'salons': SALONS,
        'products': PRODUCTS,
    }
    return render(request, 'lookby_app/landing.html', context)


def login_view(request):
    error = None
    if request.method == 'POST':
        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password') or ''
        user = next((u for u in DEMO_ACCOUNTS if u['email'].lower() == email and u['password'] == password), None)
        if user is None:
            error = 'Credenciales inválidas. Usa alguno de los accesos demo.'
        else:
            _login_user(request, user)
            return redirect(_redirect_for_role(user['role']))

    return render(request, 'lookby_app/login.html', {'demo_accounts': DEMO_ACCOUNTS, 'error': error})


def register_view(request):
    if request.method == 'POST':
        form_role = request.POST.get('role') or 'client'
        user = {
            'email': request.POST.get('email') or 'demo@lookby.cl',
            'password': request.POST.get('password') or '123456',
            'role': form_role,
            'name': request.POST.get('name') or 'Usuario LookBy',
            'display_role': {'client': 'CLIENTE', 'business': 'NEGOCIO', 'supplier': 'PROVEEDOR', 'superadmin': 'SUPERADMIN'}.get(form_role, 'CLIENTE'),
        }
        _login_user(request, user)
        return redirect(_redirect_for_role(form_role))
    return render(request, 'lookby_app/register.html', {'demo_accounts': DEMO_ACCOUNTS})


def recover_view(request):
    message = None
    if request.method == 'POST':
        email = (request.POST.get('email') or '').strip()
        if email:
            message = f'Se ha enviado un enlace de recuperación a {email}. En entorno local se muestra este mensaje.'
    return render(request, 'lookby_app/recover.html', {'message': message})


def reset_password_view(request):
    success = False
    if request.method == 'POST':
        password = request.POST.get('password') or ''
        confirm = request.POST.get('confirm_password') or ''
        if password and password == confirm:
            success = True
    return render(request, 'lookby_app/reset_password.html', {'success': success})


def logout_view(request):
    request.session.flush()
    return redirect('home')


def _default_user_for_role(role):
    defaults = {
        'client': {
            'name': 'Sofía Alarcón',
            'email': 'cliente@lookby.cl',
            'role': 'client',
            'display_role': 'CLIENTE',
        },
        'business': {
            'name': 'Atelier Doré',
            'email': 'negocio@lookby.cl',
            'role': 'business',
            'display_role': 'NEGOCIO',
        },
        'supplier': {
            'name': 'Luna Supply',
            'email': 'proveedor@lookby.cl',
            'role': 'supplier',
            'display_role': 'PROVEEDOR',
        },
        'superadmin': {
            'name': 'Valeria Ramos',
            'email': 'admin@lookby.cl',
            'role': 'superadmin',
            'display_role': 'SUPERADMIN',
        },
    }
    return defaults.get(role, defaults['client'])


def _dashboard(request, role, template_name):
    user = _get_session_user(request) or _default_user_for_role(role)
    context = {
        'user': user,
        'stats': [
            {'label': 'Citas agendadas', 'value': '3'},
            {'label': 'Pedidos', 'value': '6'},
            {'label': 'Calificación', 'value': '4.8'},
        ],
    }
    return render(request, template_name, context)


def client_dashboard(request):
    return _dashboard(request, 'client', 'lookby_app/client_dashboard.html')


def business_dashboard(request):
    return _dashboard(request, 'business', 'lookby_app/business_dashboard.html')


def supplier_dashboard(request):
    return _dashboard(request, 'supplier', 'lookby_app/supplier_dashboard.html')


def superadmin_dashboard(request):
    return _dashboard(request, 'superadmin', 'lookby_app/superadmin_dashboard.html')
