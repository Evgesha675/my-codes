let phoneCount = 2;

function addPhoneField() {
    const phoneFields = document.querySelector('.phone-fields');
    const newPhoneField = document.createElement('div');
    newPhoneField.classList.add('phone-field');
    newPhoneField.innerHTML = `
        <label for="phone${phoneCount}">Дополнительный телефон:</label>
        <input type="tel" id="phone${phoneCount}">
    `;
    phoneFields.appendChild(newPhoneField);
    phoneCount++;
}

function updatePreview() {
    const organization = document.getElementById('organization').value;
    const fullName = document.getElementById('fullName').value;
    const position = document.getElementById('position').value;
    const phone1 = document.getElementById('phone1').value;
    const phone2 = document.getElementById('phone2').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const fontSize = document.getElementById('fontSize').value + 'px';
    const fontWeight = document.getElementById('fontWeight').value;
    const fontColor = document.getElementById('fontColor').value;
    const bgColor = document.getElementById('bgColor').value;

    const businessCard = document.getElementById('business-card');
    businessCard.innerHTML = `
        <div style="background-color: ${bgColor}; padding: 10px; box-sizing: border-box; height: 100%;">
            <div style="text-align: center; margin-bottom: 10px;">
                <div style="font-size: ${fontSize}; font-weight: bold; color: ${fontColor};">${organization}</div>
                <div style="font-size: ${fontSize}; font-weight: ${fontWeight}; color: ${fontColor};">${fullName}</div>
                <div style="font-size: ${fontSize}; font-weight: ${fontWeight}; color: ${fontColor};">${position}</div>
            </div>
            <div style="display: flex; flex-direction: column; text-align: right;">
                <div style="font-size: ${fontSize}; color: ${fontColor};">${phone1}</div>
                <div style="font-size: ${fontSize}; color: ${fontColor};">${phone2}</div>
                <div style="font-size: ${fontSize}; color: ${fontColor};">${email}</div>
                <div style="font-size: ${fontSize}; color: ${fontColor};">${address}</div>
            </div>
        </div>
    `;
}
