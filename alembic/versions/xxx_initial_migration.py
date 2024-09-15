from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create the bands table
    op.create_table(
        'bands',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('hometown', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create the venues table
    op.create_table(
        'venues',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create the concerts table with foreign keys
    op.create_table(
        'concerts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.String(), nullable=False),
        sa.Column('band_id', sa.Integer(), nullable=False),
        sa.Column('venue_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['band_id'], ['bands.id']),
        sa.ForeignKeyConstraint(['venue_id'], ['venues.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Drop the concerts table
    op.drop_table('concerts')

    # Drop the venues table
    op.drop_table('venues')

    # Drop the bands table
    op.drop_table('bands')
