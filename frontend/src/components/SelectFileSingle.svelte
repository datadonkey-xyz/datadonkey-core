<script lang="ts">
	import { FileUploader, FileUploaderButton, Modal } from "carbon-components-svelte";

  export let type: "image" | "data" = "image";
  export let files: File[] = [];

</script>

<FileUploader 
  multiple={false}
  buttonLabel={`Upload ${type == 'image' ? 'image' : 'file'}`}
  status="complete"
  accept={(() => {
    switch (type) {
      case "image": {
        return [".jpg", ".jpeg", ".png", ".tiff"]
      }
      case "data": {
        return [".csv", ".xlsx"]
      }
    }
  })()}
  bind:files
/>
