"""Add users column

Revision ID: 22eefe5c7b63
Revises: 3168880bdb9d
Create Date: 2024-07-06 11:06:39.949881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22eefe5c7b63'
down_revision: Union[str, None] = '3168880bdb9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('date_of_birth', sa.Date))


def downgrade() -> None:
    op.drop_column('users', 'date_of_birth')
