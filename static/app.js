// app.js
$(document).ready(function(){
  const endpoint = '/predict_asthma'; // same server

  $('#asthmaForm').on('submit', async function(e){
    e.preventDefault();
    $('#message').text('');
    $('#result').text('');

    // read values
    const bmi = parseFloat($('#bmi').val());
    const family_history = parseInt($('#family_history').val());
    const smoking_status = $('#smoking_status').val();
    const allergies = $('#allergies').val();
    const air_pollution_level = $('#air_pollution_level').val();
    const physical_activity_level = $('#physical_activity_level').val();

    // simple validation
    if (isNaN(bmi)) return $('#message').text('Please enter a valid BMI value.');
    if (bmi < 15 || bmi > 45) return $('#message').text('BMI must be between 15 and 45.');
    if (![0,1].includes(family_history)) return $('#message').text('Select Family History (0 or 1).');
    if (!smoking_status) return $('#message').text('Select Smoking Status.');
    if (!allergies) return $('#message').text('Select Allergies.');
    if (!air_pollution_level) return $('#message').text('Select Air Pollution Level.');
    if (!physical_activity_level) return $('#message').text('Select Physical Activity Level.');

    // NOTE: keys here are capitalized to match your app.py expectations
    const payload = {
      "BMI": bmi,
      "Family_History": family_history,
      "Smoking_Status": smoking_status,
      "Allergies": allergies,
      "Air_Pollution_Level": air_pollution_level,
      "Physical_Activity_Level": physical_activity_level
    };

    // UI feedback
    $('#predictBtn').prop('disabled', true).text('Predicting...');

    try {
      const resp = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const data = await resp.json();

      if (!resp.ok) {
        const err = data.error || JSON.stringify(data);
        $('#message').text('Error: ' + err);
      } else {
        // ensure asthma_result exists and is numeric
        const resultVal = data.asthma_result;
        const probVal = data.probability;
        const label = (resultVal === 1 || resultVal === '1') ? 'Likely Asthma' : 'Unlikely Asthma';
        const prob = (typeof probVal === 'number') ? (probVal * 100).toFixed(2) + '%' : JSON.stringify(probVal);
        $('#result').html(`<strong>Prediction:</strong> ${label} <br/><strong>Probability:</strong> ${prob}`);
      }

    } catch (err) {
      console.error(err);
      $('#message').text('Network error: Could not reach the server.');
    } finally {
      $('#predictBtn').prop('disabled', false).text('Predict Asthma');
    }
  });
});
