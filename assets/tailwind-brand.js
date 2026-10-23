/* Structural Sensei brand palette for the Tailwind CDN.
   Load right AFTER https://cdn.tailwindcss.com
   Remaps the existing blue/red/orange/gray classes so no markup has to change. */
tailwind.config = {
  theme: {
    extend: {
      colors: {
        // old "blue" accent -> brand orange (logo sun + wordmark swoosh)
        blue: {
          300: '#ffc27a',
          400: '#ff9a45',
          500: '#f47b20',
          600: '#e4501e',
          700: '#c2410c',
          800: '#9a3412',
          900: '#5a1a0a'
        },
        // red -> logo red-orange
        red: {
          400: '#ff7a4d',
          500: '#e8501f',
          600: '#d94a1e',
          900: '#4a1608'
        },
        orange: {
          400: '#ff9a45',
          500: '#f47b20',
          600: '#e4501e'
        },
        // neutral blacks (no blue tint)
        gray: {
          700: '#2a2a2a',
          800: '#171717',
          900: '#0c0c0c',
          950: '#050505'
        }
      },
      fontFamily: {
        display: ['Anton', 'Impact', 'Arial Narrow', 'sans-serif'],
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif']
      }
    }
  }
};
