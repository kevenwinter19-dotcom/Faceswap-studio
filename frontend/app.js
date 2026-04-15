class FaceSwapApp {
    constructor() {
        this.init();
    }
    
    init() {
        this.videoInput = document.getElementById('videoInput');
        this.faceInput = document.getElementById('faceInput');
        this.processBtn = document.getElementById('processBtn');
        
        this.bindEvents();
    }
    
    bindEvents() {
        document.querySelectorAll('.upload-zone').forEach(zone => {
            zone.addEventListener('click', () => zone.querySelector('input').click());
            ['dragover', 'dragenter'].forEach(evt => 
                zone.addEventListener(evt, e => e.preventDefault())
            );
        });
        
        this.videoInput.onchange = (e) => this.onFileSelect(e, 'video');
        this.faceInput.onchange = (e) => this.onFileSelect(e, 'face');
        this.processBtn.onclick = () => this.process();
    }
    
    onFileSelect(event, type) {
        console.log(`${type} file selected`);
        if (this.videoInput.files[0] && this.faceInput.files[0]) {
            this.processBtn.disabled = false;
        }
    }
    
    async process() {
        const formData = new FormData();
        formData.append('video', this.videoInput.files[0]);
        formData.append('face_image', this.faceInput.files[0]);
        
        this.processBtn.disabled = true;
        this.processBtn.textContent = 'Processing...';
        
        try {
            const response = await fetch('/api/upload', { method: 'POST', body: formData });
            const data = await response.json();
            
            await fetch(`/api/process/${data.session_id}`, { method: 'POST' });
            console.log('Processing started');
        } catch (error) {
            console.error('Error:', error);
        }
    }
}

new FaceSwapApp();
