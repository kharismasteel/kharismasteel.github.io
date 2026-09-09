/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.{html,md,markdown}',
    './_includes/**/*.{html,md,markdown}',
    './_layouts/**/*.{html,md,markdown}',
    './_posts/**/*.{html,md,markdown}',
    './_products/**/*.{html,md,markdown}',
    './archive/**/*.{html,md,markdown}',
    './products/**/*.{html,md,markdown}'
  ],
  theme: {
    extend: {}
  },
  plugins: []
};
