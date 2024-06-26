"""empty message

Revision ID: 6908358bb771
Revises: e7d940747a6c
Create Date: 2024-06-01 00:56:44.598962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6908358bb771'
down_revision = 'e7d940747a6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('cause', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient', 'cause')
    # ### end Alembic commands ###
