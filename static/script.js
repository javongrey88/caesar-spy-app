window.addEventListener("DOMContentLoaded", () => {
    const resultBlocks = document.querySelectorAll(".output p");
    resultBlocks.forEach((block) => typeWriter(block));

    function typeWriter(element) {
        const text = element.textContent;
        element.textContent = "";
        let i = 0;
        const speed = 40;

        function typing() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(typing, speed);
            }
        }

        typing();
    }
});
