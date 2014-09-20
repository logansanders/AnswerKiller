"""empty message

Revision ID: 3e5b592c6434
Revises: 445eae9f1633
Create Date: 2014-09-20 18:29:02.725597

"""

# revision identifiers, used by Alembic.
revision = '3e5b592c6434'
down_revision = '445eae9f1633'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('textbooks', sa.Column('image_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('textbooks', 'image_id')
    ### end Alembic commands ###