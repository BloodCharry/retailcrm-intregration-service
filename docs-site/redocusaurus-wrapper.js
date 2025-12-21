// redocusaurus-wrapper.js
async function RedocWrapper(...args) {
  const mod = await import('redocusaurus');


  let pluginFn = mod.default?.default || mod.default || mod.redocusaurus;

  if (typeof pluginFn !== 'function') {
    console.error('Could not find redocusaurus function. Module:', mod);
    throw new Error('redocusaurus is not a function');
  }

  const plugin = await pluginFn(...args);

  if (!plugin.name) {
    plugin.name = 'redocusaurus';
  }

  return plugin;
}

RedocWrapper.name = 'redocusaurus';

module.exports = RedocWrapper;