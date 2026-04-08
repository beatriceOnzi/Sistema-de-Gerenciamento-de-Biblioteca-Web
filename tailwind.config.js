/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./static/**/*.{js}"],
  theme: {
    extend: {
      colors: {
        'amarelo_cnec': '#ffd32b',
        cnec:{
          amarelo: '#ffd32b',
          azul: '#1c1f53',
          branco: '#F2F2F0',
          azul_claro: '#5f9ae1'
        }
      }
    },
  },
  plugins: [],
}

