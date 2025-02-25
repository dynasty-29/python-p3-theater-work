from sqlalchemy.orm import sessionmaker
from models import engine, Role, Audition, Session

# Create a new session
session = Session()

# roles
roles = [
    Role(name="Yoo Si-jin for Descendants of the Sun"),
    Role(name="Hong Hae-in for Queen of Tears"),
    Role(name="Park Sae-ro-yi for Itaewon Class"),
    Role(name="Seong Gi-hun for Squid Game"),
    Role(name="Gu Jun-pyo for Boys Over Flowers")
]
session.add_all(roles)
session.commit()

# auditions
auditions = [
    Audition(actor="Song Joong-ki", location="Seoul", phone=123456789, role_id=roles[0].id),
    Audition(actor="Kim Ji-won", location="Busan", phone=987654321, role_id=roles[0].id),
    Audition(actor="Kim Soo-hyun", location="Incheon", phone=111222333, role_id=roles[1].id),
    Audition(actor="Park Seo-joon", location="Seoul", phone=444555666, role_id=roles[2].id),
    Audition(actor="Lee Jung-jae", location="Seoul", phone=777888999, role_id=roles[3].id),
    Audition(actor="Lee Min-ho", location="Daegu", phone=666555444, role_id=roles[4].id)
]
session.add_all(auditions)
session.commit()

print("Database seeded successfully!")