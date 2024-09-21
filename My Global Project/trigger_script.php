<?php
// Path to your Python script
$pythonScript = 'C:\\Users\\meera\\Documents\\BTech CSE spl. AIML\\VS code\\TempScale - Entropy \'24\\My Global Project\\app.py';

// Execute the Python script
exec("python \"$pythonScript\" 2>&1", $output, $return_var);

// Return a response based on the result
if ($return_var === 0) {
    echo "Success";
} else {
    echo "Failure";
}
?>
