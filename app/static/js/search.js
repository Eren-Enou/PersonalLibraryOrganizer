document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('#tag-container .tag');

    // Object to hold the state of each tag
    let tagStates = {};

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            event.preventDefault();
            const tagValue = this.getAttribute('data-value');

            // Determine the current state and toggle to the next one
            switch (tagStates[tagValue]) {
                case 'included':
                    tagStates[tagValue] = 'excluded';
                    this.classList.remove('included');
                    this.classList.add('excluded');
                    break;
                case 'excluded':
                    delete tagStates[tagValue]; // Remove from object, effectively "unselecting" it
                    this.classList.remove('excluded');
                    break;
                default:
                    tagStates[tagValue] = 'included';
                    this.classList.add('included');
            }

            // Optionally, update hidden inputs to reflect the current state of selections
            updateHiddenInputs();
        });
    });

    function updateHiddenInputs() {
        // Assuming you have hidden inputs for included and excluded tags
        const includedInput = document.getElementById('included_tag_names');
        const excludedInput = document.getElementById('excluded_tag_names');

        // Filter the tagStates object to get included and excluded tags, then update the hidden inputs
        includedInput.value = Object.keys(tagStates).filter(key => tagStates[key] === 'included').join(',');
        excludedInput.value = Object.keys(tagStates).filter(key => tagStates[key] === 'excluded').join(',');
    }
    // Initialize Select2 on your fields
    $('#publication_demographic').select2();
    $('#status').select2();
    $('#content_rating').select2();
});

