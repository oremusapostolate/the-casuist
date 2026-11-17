plugins: [
        // Turns |13| into <span id="p-13" class="page-marker">p. 13</span>
        function(hook) {
          hook.beforeEach(function(html) {
            return html.replace(
              /\|(\d+)\|/g,
              '<span id="p-$1" class="page-marker" title="Printed Page $1">p. $1</span>'
            );
          });
        }
      ]