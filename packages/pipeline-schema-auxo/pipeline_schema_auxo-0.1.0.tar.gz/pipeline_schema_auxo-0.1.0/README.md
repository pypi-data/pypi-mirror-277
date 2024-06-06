# Pipeline Schema Auxo

A description of your package.

## Installation

```bash
pip install your_package

```

## Usage

```
from your_package import User, ClinicalTrial, Claim, Payment, Session

# Create a new session
session = Session()

# Example of adding a new user
new_user = User(username='example_user', npi=123456)
session.add(new_user)
session.commit()

# Example of adding a new clinical trial
new_trial = ClinicalTrial(user_id=new_user.id, trial_name='Trial 1', status='ongoing')
session.add(new_trial)
session.commit()

# Similarly, you can add claims and payments
```