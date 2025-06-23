module.exports = async (io) => {
  await io.rmRF('src');
  const path = `packages/${process.env.GITHUB_WORKFLOW_REF.match(/\/([^/]+)\.\w+@/)[1]}`
  await io.mv(`${path}/pyproject.toml`, '.', {force: true});
  await io.mv(`${path}/README.md`, '.', {force: true});
  await io.mv(`${path}/CMakeLists.txt`, '.');
  io.mkdirP(`${path}/src`)
  await io.mv(`${path}/src`, '.', {recursive: true});
}
