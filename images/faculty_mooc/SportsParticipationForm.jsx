import React, { useState, useCallback } from "react";
import {
  Flex,
  FormLabel,
  Input,
  Button,
  Box,
  Heading,
  VStack,
  HStack,
  useToast,
} from "@chakra-ui/react";
import axios from "axios";

const SportsParticipationForm = () => {
  const [formFields, setFormFields] = useState({
    reg_no: "",
    student_name: "",
    sports_event: "",
    organizing_institution: "",
    city: "",
    country: "",
    award: "",
    date_from: "",
    date_to: "",
    proof: null,
  });

  const toast = useToast();

  const handleInputChange = useCallback((event) => {
    const { name, value } = event.target;
    setFormFields((prevFields) => ({ ...prevFields, [name]: value }));
  }, []);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setFormFields((prevFields) => ({ ...prevFields, proof: file }));
  };

  const handleSubmit = useCallback(
    async (event) => {
      event.preventDefault();

      const formData = new FormData();
      Object.keys(formFields).forEach((key) => {
        if (formFields[key] !== null && formFields[key] !== '') {
          formData.append(key, formFields[key]);
        }
      });

      try {
        const response = await axios.post(
          "http://localhost:8000/api/student-sports/",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjM1NjU5LCJpYXQiOjE3MjMyMzIwNTksImp0aSI6ImE4NTYwNGQ2OTE2NTQzYTU4NWZlNzZiZDY3N2MwOWUxIiwidXNlcl9pZCI6MX0.64JEw9QJX3xORm3Q86XzI_yiLY2tsHit9qoVv-eEuXg", // Replace with actual token
            },
          }
        );

        if (response.status === 201) {
          console.log("Data submitted successfully");
          toast({
            title: "Submission Successful",
            description: "The data has been submitted successfully.",
            status: "success",
            duration: 5000,
            isClosable: true,
          });
        } else {
          console.error("Error submitting data:", response.statusText);
          toast({
            title: "Submission Error",
            description: `Unexpected response status: ${response.status}`,
            status: "error",
            duration: 5000,
            isClosable: true,
          });
        }
      } catch (error) {
        console.error("Error submitting data:", error);
        if (error.response) {
          console.error("Response data:", error.response.data);
          console.error("Response status:", error.response.status);
          console.error("Response headers:", error.response.headers);
        }
        toast({
          title: "Submission Failed",
          description: "There was an error submitting the data. Please try again.",
          status: "error",
          duration: 5000,
          isClosable: true,
        });
      }
    },
    [formFields, toast]
  );

  const handleReset = useCallback(() => {
    setFormFields({
      reg_no: "",
      student_name: "",
      sports_event: "",
      organizing_institution: "",
      city: "",
      country: "",
      award: "",
      date_from: "",
      date_to: "",
      proof: null,
    });
  }, []);

  const FormField = ({ label, inputType, name, value, onChange }) => (
    <HStack w="100%">
      <FormLabel htmlFor={name} flex="1">
        {label}
      </FormLabel>
      <Input
        type={inputType}
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        flex="2"
      />
    </HStack>
  );

  return (
    <Flex
      direction="column"
      align="center"
      justify="center"
      minHeight="100vh"
      bg="gray.50"
      p={6}
    >
      <Box p={8} rounded="md" w="full" maxW="700px">
        <Heading as="h3" size="lg" mb={6} textAlign="center">
          Participation in Sports Activities
        </Heading>
        <form onSubmit={handleSubmit}>
          <VStack spacing={6}>
            <FormField
              label="Registration No:"
              inputType="text"
              name="reg_no"
              value={formFields.reg_no}
              onChange={handleInputChange}
            />
            <FormField
              label="Name:"
              inputType="text"
              name="student_name"
              value={formFields.student_name}
              onChange={handleInputChange}
            />
            <FormField
              label="Sports Event:"
              inputType="text"
              name="sports_event"
              value={formFields.sports_event}
              onChange={handleInputChange}
            />
            <FormField
              label="Organizing Institution:"
              inputType="text"
              name="organizing_institution"
              value={formFields.organizing_institution}
              onChange={handleInputChange}
            />
            <FormField
              label="City:"
              inputType="text"
              name="city"
              value={formFields.city}
              onChange={handleInputChange}
            />
            <FormField
              label="Country:"
              inputType="text"
              name="country"
              value={formFields.country}
              onChange={handleInputChange}
            />
            <HStack w="100%">
              <FormLabel flex="1">Date From:</FormLabel>
              <Input
                type="date"
                name="date_from"
                value={formFields.date_from}
                onChange={handleInputChange}
                flex="2"
              />
            </HStack>
            <HStack w="100%">
              <FormLabel flex="1">Date To:</FormLabel>
              <Input
                type="date"
                name="date_to"
                value={formFields.date_to}
                onChange={handleInputChange}
                flex="2"
              />
            </HStack>
            <HStack w="100%">
              <FormLabel flex="1">Award (if any):</FormLabel>
              <Input
                type="text"
                name="award"
                value={formFields.award}
                onChange={handleInputChange}
                flex="2"
              />
            </HStack>
            <HStack w="100%">
              <FormLabel flex="1">Upload Proof:</FormLabel>
              <Input
                type="file"
                name="proof"
                onChange={handleFileChange}
                flex="2"
              />
            </HStack>
            <HStack spacing={4} pt={4}>
              <Button type="submit">Submit</Button>
              <Button variant="outline" colorScheme="red" onClick={handleReset}>
                Reset
              </Button>
            </HStack>
          </VStack>
        </form>
      </Box>
    </Flex>
  );
};

export default SportsParticipationForm;
