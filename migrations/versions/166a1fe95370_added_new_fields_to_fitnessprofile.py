"""Added new fields to FitnessProfile

Revision ID: 166a1fe95370
Revises: 
Create Date: 2023-07-29 16:32:35.199334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '166a1fe95370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fitness_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preferred_workout_duration', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('gym_or_home', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('equipment', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fitness_profile', schema=None) as batch_op:
        batch_op.drop_column('equipment')
        batch_op.drop_column('gym_or_home')
        batch_op.drop_column('preferred_workout_duration')

    # ### end Alembic commands ###