import { defineConfig, presetUno, presetIcons, presetTypography, presetWebFonts } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetIcons({
      collections: {
        mdi: () => import('@iconify/json/json/mdi.json').then(i => i.default),
        carbon: () => import('@iconify/json/json/carbon.json').then(i => i.default),
      }
    }),
    presetTypography(),
    presetWebFonts({
      fonts: {
        sans: ['Inter', 'Noto Sans SC'],
        mono: ['JetBrains Mono', 'Fira Code'],
      }
    })
  ],
  theme: {
    colors: {
      primary: {
        50: '#eff6ff',
        100: '#dbeafe',
        200: '#bfdbfe',
        300: '#93c5fd',
        400: '#60a5fa',
        500: '#3b82f6',
        600: '#2563eb',
        700: '#1d4ed8',
        800: '#1e40af',
        900: '#1e3a8a',
      }
    }
  },
  shortcuts: {
    'btn': 'px-4 py-2 rounded-lg font-medium transition-all duration-200',
    'btn-primary': 'btn bg-primary-600 text-white hover:bg-primary-700 active:bg-primary-800',
    'btn-secondary': 'btn bg-gray-200 text-gray-800 hover:bg-gray-300 active:bg-gray-400',
    'input': 'px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent',
    'card': 'bg-white rounded-lg shadow-sm border border-gray-200 p-4',
    'search-card': 'card hover:shadow-md transition-shadow duration-200 cursor-pointer',
  }
})