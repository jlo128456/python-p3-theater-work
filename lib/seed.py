from models import session, Role, Audition

# Sample role
role = Role(character_name="Hamlet")
session.add(role)
session.commit()

# Auditions for that role
a1 = Audition(actor="Alice", location="NYC", phone=1234567890, hired=False, role=role)
a2 = Audition(actor="Bob", location="LA", phone=9876543210, hired=True, role=role)
session.add_all([a1, a2])
session.commit()

print("Seeded theater_work.db with sample data.")