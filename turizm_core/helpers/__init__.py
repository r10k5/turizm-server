from django.contrib.auth.decorators import user_passes_test

has_role = lambda roles: user_passes_test(lambda u: u.role.id in roles)
is_tour_operator = has_role(['tour_operator'])
is_manager = has_role(['manager'])
is_admin = has_role(['admin'])