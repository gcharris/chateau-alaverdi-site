/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html","./src/**/*.{js,ts,jsx,tsx}"],
  theme: { 
    extend: {
      colors: {
        bordeaux: '#722F37',
        gold: '#D4AF37',
        cream: '#F5F5DC'
      },
      fontFamily: {
        'playfair': ['Playfair Display', 'serif'],
        'lato': ['Lato', 'sans-serif']
      }
    } 
  },
  plugins: [],
};
