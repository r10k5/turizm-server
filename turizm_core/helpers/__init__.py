from django.contrib.auth.decorators import user_passes_test

is_tour_operator = user_passes_test(lambda u: u.role.id == 'tour_operator')
is_manager = user_passes_test(lambda u: u.role.id == 'manager')
is_admin = user_passes_test(lambda u: u.role.id == 'admin')