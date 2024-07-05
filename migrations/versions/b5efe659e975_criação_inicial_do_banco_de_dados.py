"""Criação inicial do banco de dados

Revision ID: b5efe659e975
Revises: 
Create Date: 2024-07-02 09:55:35.409786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5efe659e975'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curriculo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('temp_field', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curriculo', schema=None) as batch_op:
        batch_op.drop_column('temp_field')

    # ### end Alembic commands ###
