// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import viteTsconfigPaths from 'vite-tsconfig-paths';
import svgrPlugin from 'vite-plugin-svgr';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react(), viteTsconfigPaths(), svgrPlugin()],
  server: {
    proxy: {
      '/api': 'http://localhost:5000',
    },
    port: 3000,
    watch: {
      usePolling: true,
    }
  },
})