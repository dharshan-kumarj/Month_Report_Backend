import React, { useState, useCallback } from "react";
import axios from 'axios';
import { Input, Text, Heading, Flex, Stack, Button, useToast } from "@chakra-ui/react";
import Navbar from "../Component/navigationbar";

const FormField = ({ label, inputType, placeholder, value, onChange }) => {
  return (
    <Flex align="center" marginBottom={4}>
      <Text fontSize="md" width="200px" textAlign="justify" marginRight={100}>
        {label}
      </Text>
      <Input
        type={inputType}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        htmlSize={14}
        width="300px"
      />
    </Flex>
  );
};

const Main = () => {
  const [formData, setFormData] = useState({
    student_name: "",
    reg_no: "",
    project_title: "",
    amount_sanctioned: "",
    letter_no: "",
    sanction_date: "",
    period_from: "",
    period_to: "",
  });
  const [proofFile, setProofFile] = useState(null);

  const toast = useToast();

  const handleInputChange = useCallback((field, value) => {
    setFormData(prevData => ({ ...prevData, [field]: value }));
  }, []);

  const handleFileChange = (event) => {
    setProofFile(event.target.files[0]);
  };

  const handleSubmit = useCallback(async (event) => {
    event.preventDefault();
    
    // Format the data as per the requested JSON structure
    const formattedData = {
      student_name: formData.student_name,
      reg_no: formData.reg_no,
      project_title: formData.project_title,
      amount_sanctioned: parseFloat(formData.amount_sanctioned),
      letter_no_and_date: `${formData.letter_no} dated ${formData.sanction_date}`,
      period: `${getDurationInMonths(formData.period_from, formData.period_to)} months (${formatDate(formData.period_from)} - ${formatDate(formData.period_to)})`
    };

    const submissionData = new FormData();
    Object.keys(formattedData).forEach(key => {
      submissionData.append(key, formattedData[key]);
    });
    if (proofFile) {
      submissionData.append('proof', proofFile);
    }

    try {
      const response = await axios.post(
        'http://localhost:8000/api/student-seed-money/',
        submissionData,
        {
          headers: {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjMwMDY2LCJpYXQiOjE3MjMyMjY0NjYsImp0aSI6ImU2MDcwMDBjYjI0MDQ4ZjZhZWUwZWE2M2Q4YTAzZjU5IiwidXNlcl9pZCI6MX0.YAciYxMLRCr4vpizME-tR54FfqpS6Pc2fkeU4qOjmEc',
            'Content-Type': 'multipart/form-data',
          },
        }
      );
      console.log('Submitted Data:', response.data);
      toast({
        title: "Submission Successful",
        description: "Seed money grant data has been submitted.",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Error submitting data:', error);
      if (error.response) {
        console.error('Server response:', error.response.data);
      }
      toast({
        title: "Submission Failed",
        description: "There was an error submitting the data. Please try again.",
        status: "error",
        duration: 5000,
        isClosable: true,
      });
    }
  }, [formData, proofFile, toast]);

  // Helper function to calculate duration in months
  const getDurationInMonths = (startDate, endDate) => {
    const start = new Date(startDate);
    const end = new Date(endDate);
    return (end.getFullYear() - start.getFullYear()) * 12 + end.getMonth() - start.getMonth() + 1;
  };

  // Helper function to format date as "Month Year"
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('default', { month: 'long', year: 'numeric' });
  };

  const handleReset = useCallback(() => {
    setFormData({
      student_name: "",
      reg_no: "",
      project_title: "",
      amount_sanctioned: "",
      letter_no: "",
      sanction_date: "",
      period_from: "",
      period_to: "",
    });
    setProofFile(null);
  }, []);

  return (
    <>
      <Navbar />
      <Flex direction="column" align="center" justify="center" height="100vh" className="mains">
        <div className="mains">
          <Heading textAlign="center" mb={4}>
            Seed Money Grant for Students from the Management
          </Heading>
          <hr />
          <br />
          <Flex justify='center'>
            <form onSubmit={handleSubmit}>
              <div className="titles">
                <FormField
                  label="Name of the Student:"
                  inputType="text"
                  placeholder="Enter student name"
                  value={formData.student_name}
                  onChange={(e) => handleInputChange("student_name", e.target.value)}
                />
                <FormField
                  label="Registration Number:"
                  inputType="text"
                  placeholder="Enter registration number"
                  value={formData.reg_no}
                  onChange={(e) => handleInputChange("reg_no", e.target.value)}
                />
                <FormField
                  label="Title of the Project:"
                  inputType="text"
                  placeholder="Enter project title"
                  value={formData.project_title}
                  onChange={(e) => handleInputChange("project_title", e.target.value)}
                />
                <FormField
                  label="Amount Sanctioned:"
                  inputType="number"
                  placeholder="₹"
                  value={formData.amount_sanctioned}
                  onChange={(e) => handleInputChange("amount_sanctioned", e.target.value)}
                />
                <FormField
                  label="Letter No:"
                  inputType="text"
                  placeholder="Enter letter number"
                  value={formData.letter_no}
                  onChange={(e) => handleInputChange("letter_no", e.target.value)}
                />
                <FormField
                  label="Date of Sanction:"
                  inputType="date"
                  value={formData.sanction_date}
                  onChange={(e) => handleInputChange("sanction_date", e.target.value)}
                />
                <FormField
                  label="Period From:"
                  inputType="date"
                  value={formData.period_from}
                  onChange={(e) => handleInputChange("period_from", e.target.value)}
                />
                <FormField
                  label="Period To:"
                  inputType="date"
                  value={formData.period_to}
                  onChange={(e) => handleInputChange("period_to", e.target.value)}
                />
                <Flex align="center" marginBottom={4}>
                  <Text fontSize="md" width="200px" textAlign="justify" marginRight={100}>
                    Proof:
                  </Text>
                  <Input
                    type="file"
                    onChange={handleFileChange}
                    width="300px"
                  />
                </Flex>
              </div>
              <Stack spacing={220} direction="row" marginTop={10}>
                <Button colorScheme="green" type="submit">
                  Submit
                </Button>
                <Button colorScheme="teal" variant="outline" onClick={handleReset}>
                  Reset
                </Button>
              </Stack>
            </form>
          </Flex>
        </div>
      </Flex>
    </>
  );
};

export default Main;