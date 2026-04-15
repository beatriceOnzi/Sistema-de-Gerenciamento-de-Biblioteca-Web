/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./static/**/*.{js}"],
  theme: {
    extend: {
      colors: {
        'amarelo_cnec': '#ffc023',
        cnec:{
          amarelo: '#ffd32b',
          azul: {
            DEFAULT: '#003c9d',
            claro: '#7c89c2',
            escuro: "#0e1133"
          },
          branco: '#F2F2F0'
        }
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif']
      }
    },
  },
  plugins: [],
}

