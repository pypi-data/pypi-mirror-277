class LinkTargetBlockDefinition extends window.wagtailStreamField.blocks.StructBlockDefinition {
  render(placeholder, prefix, initialState, initialError) {
    const block = super.render(
      placeholder,
      prefix,
      initialState,
      initialError,
    );

    const typeInput = block.childBlocks.type.widget.input[0];

    // Retrieve child blocks from meta definition
    const childBlocks = this.meta.blockTypes.map((name) => block.childBlocks[name]);

    const updateChildBlocks = () => {
      childBlocks.forEach(({ type, element }) => {
        element.hidden = type !== typeInput.value;  // eslint-disable-line no-param-reassign
      });
    };

    // Set initial hidden state of child blocks
    updateChildBlocks();

    typeInput.addEventListener('change', updateChildBlocks);

    return block;
  }
}

window.telepath.register('wagtail_cblocks.blocks.LinkTargetBlock', LinkTargetBlockDefinition);
