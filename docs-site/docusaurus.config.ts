import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'RetailCRM Integration Service',
  tagline: 'API & Docs',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },
  // для локального запуска
  // url: 'http://localhost:3001',
  // baseUrl: '/',
  // для docker-compose
  url: 'http://localhost',
  baseUrl: '/docs-site/',

  organizationName: 'your-org',
  projectName: 'retailcrm-intregration-service',

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ru'],
  },

  presets: [
  [
    'redocusaurus',
    {
      specs: [
        {
          id: 'retailcrm-api',
          // для локального запуска
          // spec: 'http://127.0.0.1:8000/openapi.json',
          // для docker-compose.yml
          spec: './static/openapi.json',
          route: '/api',
        },
      ],
      theme: {
        primaryColor: '#2E8555',
      },
    },
  ],
  [
    'classic',
    {
      docs: {
        sidebarPath: './sidebars.ts',
        editUrl: 'https://github.com/BloodCharry/retailcrm-intregration-service/tree/main/docs-site/',
      },
      blog: { showReadingTime: true },
      theme: { customCss: './src/css/custom.css' },
    } satisfies Preset.Options,
  ],
],


  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'RetailCRM Docs',
      logo: {
        alt: 'RetailCRM Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        { to: '/blog', label: 'Blog', position: 'left' },
        { to: '/api', label: 'API Reference', position: 'left' },
        {
          href: 'https://github.com/BloodCharry/retailcrm-intregration-service',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [{ label: 'API Reference', to: '/api' }],
        },
        {
          title: 'Community',
          items: [
            { label: 'Stack Overflow', href: 'https://stackoverflow.com' },
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} RetailCRM Integration Service`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;