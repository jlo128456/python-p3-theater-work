
import ipdb
from models import session, Role, Audition

# Optionally, load a few things to start exploring
roles = session.query(Role).all()
auditions = session.query(Audition).all()

print(f"Loaded {len(roles)} roles and {len(auditions)} auditions into memory.")
print("You can explore using variables: roles, auditions, session, etc.")

# Start interactive shell
ipdb.set_trace()