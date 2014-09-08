"""empty message

Revision ID: 4f1b7e8d4fd5
Revises: 1bfb66db1f3b
Create Date: 2014-09-08 14:13:27.294513

"""

# revision identifiers, used by Alembic.
revision = '4f1b7e8d4fd5'
down_revision = '1bfb66db1f3b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('min_fee', sa.Float(precision=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path')
    )
    op.create_table('accounts',
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('nickname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('intro', sa.String(length=120), nullable=True),
    sa.Column('gender', sa.Enum('Male', 'Female'), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('username'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname'),
    mysql_engine='InnoDB'
    )
    op.create_table('customers',
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('school', sa.String(length=120), nullable=True),
    sa.Column('grade', sa.String(length=20), nullable=True),
    sa.Column('balance', sa.Float(precision=2), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['accounts.username'], ),
    sa.PrimaryKeyConstraint('username'),
    mysql_engine='InnoDB'
    )
    op.create_table('textbooks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_table('tutors',
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['accounts.username'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('username'),
    mysql_engine='InnoDB'
    )
    op.create_table('customer_supports',
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('permission_level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['accounts.username'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('username'),
    mysql_engine='InnoDB'
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.String(length=80), nullable=True),
    sa.Column('cs_id', sa.String(length=80), nullable=True),
    sa.Column('status', sa.Enum('Completed', 'Created', 'Paid', 'Processing'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.Column('dealine', sa.DateTime(), nullable=True),
    sa.Column('descr', sa.Text(), nullable=True),
    sa.Column('amount', sa.Float(precision=2), nullable=True),
    sa.Column('prepay', sa.Float(precision=2), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['cs_id'], ['customer_supports.username'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.username'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('chapter', sa.Integer(), nullable=False),
    sa.Column('qno', sa.Integer(), nullable=False),
    sa.Column('page', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('snapshots', sa.String(length=256), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['textbooks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_table('solving_table',
    sa.Column('tutor_username', sa.String(length=80), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.Column('actual_hours', sa.Float(precision=2), nullable=True),
    sa.Column('status', sa.Enum('Completed', 'Created', 'Paid', 'Processing'), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tutor_username'], ['tutors.username'], ),
    sa.PrimaryKeyConstraint('tutor_username', 'order_id'),
    mysql_engine='InnoDB'
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('step', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answers')
    op.drop_table('solving_table')
    op.drop_table('questions')
    op.drop_table('orders')
    op.drop_table('customer_supports')
    op.drop_table('tutors')
    op.drop_table('textbooks')
    op.drop_table('customers')
    op.drop_table('accounts')
    op.drop_table('images')
    op.drop_table('courses')
    ### end Alembic commands ###
