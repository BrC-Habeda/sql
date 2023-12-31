"""unique constraint

Revision ID: 92ed1ce8b1f6
Revises: 6cecc8561853
Create Date: 2024-01-02 08:14:30.575234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92ed1ce8b1f6'
down_revision = '6cecc8561853'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_number', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('room_number')
    )
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guest_name', sa.String(), nullable=False),
    sa.Column('check_in', sa.DateTime(timezone=True), nullable=True),
    sa.Column('check_out', sa.DateTime(timezone=True), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('room_id', 'check_in', 'check_out', name='unique_reservation')
    )
    op.add_column('addresses', sa.Column('phone_number', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('addresses', 'phone_number')
    op.drop_table('reservations')
    op.drop_table('rooms')
    # ### end Alembic commands ###
