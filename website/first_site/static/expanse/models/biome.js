class Biome {
  constructor(id, blocks) {
    this.id = id;
    this.blocks = blocks;
  }
  generate(environment) {
    const [height, temperature, humidity] = environment;
  }
}
