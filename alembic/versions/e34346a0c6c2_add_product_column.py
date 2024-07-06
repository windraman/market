"""Add product column

Revision ID: e34346a0c6c2
Revises: 22eefe5c7b63
Create Date: 2024-07-06 11:28:05.689929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e34346a0c6c2'
down_revision: Union[str, None] = '22eefe5c7b63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('rating', sa.Float))


def downgrade() -> None:
    op.drop_column('products', 'rating')
