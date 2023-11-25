from .models import User
def add_user(number):
    # Check if there are any existing User objects
    existing_users = User.objects.all()
    if existing_users.exists():
        max_id = existing_users.order_by('-card_id').first().card_id
    else:
        # If no existing users, start from card_id = 1
        max_id = 0

    start_id = max_id + 1
    for _ in range(number):
        # Create a new User object with a unique card_id
        new_user = User(card_id=start_id)
        new_user.save()
        start_id += 1
