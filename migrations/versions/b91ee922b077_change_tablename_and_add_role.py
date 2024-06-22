"""change tablename and add role

Revision ID: b91ee922b077
Revises: ab94b349f80c
Create Date: 2024-05-02 15:27:50.887949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b91ee922b077'
down_revision = 'ab94b349f80c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('doctors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Doctors_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Doctors_pkey'),
    sa.UniqueConstraint('username', name='doctors_username_key')
    )
    op.drop_table('Users')
    # ### end Alembic commands ###