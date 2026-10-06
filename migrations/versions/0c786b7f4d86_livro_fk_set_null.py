"""livro fk set null

Revision ID: 0c786b7f4d86
Revises: b3dccf15543b
Create Date: 2026-10-06 18:51:44.759410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c786b7f4d86'
down_revision = 'b3dccf15543b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('emprestimos_livro_id_fkey', 'emprestimos', type_='foreignkey')
    op.create_foreign_key('emprestimos_livro_id_fkey', 'emprestimos', 'livros', ['livro_id'], ['id'], ondelete='SET NULL')


def downgrade():
    op.drop_constraint('emprestimos_livro_id_fkey', 'emprestimos', type_='foreignkey')
    op.create_foreign_key('emprestimos_livro_id_fkey', 'emprestimos', 'livros', ['livro_id'], ['id'])
