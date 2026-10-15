import { confirmar } from './confirmacao.js'
const busca = document.getElementById('busca');
const itens = document.querySelectorAll('li[data-nome]');

document.querySelectorAll('form[data-confirmar]').forEach((form) => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault()

        const confirmado = await confirmar({
            titulo: form.dataset.titulo,
            mensagem: form.dataset.mensagem,
            textoConfirmar: form.dataset.texto
        })

        if (confirmado) form.submit()
    })
})

busca.addEventListener('input', () => {
  const termo = normalizar(busca.value);
  itens.forEach(li => {
    li.classList.toggle('hidden', !normalizar(li.dataset.nome).includes(termo));
  });
});


const normalizar = s =>
  s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();