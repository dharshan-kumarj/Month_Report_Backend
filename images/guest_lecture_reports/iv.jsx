import React, { useState, useCallback } from 'react';
import axios from 'axios';
import {
  Flex,
  FormLabel,
  Input,
  Button,
  Box,
  Heading,
  VStack,
  HStack,
  Textarea,
  useToast,
} from '@chakra-ui/react';
import Navbar from '../Component/navigationbar';

const IndustrialVisitForm = () => {
  const [formData, setFormData] = useState({
    place_of_visit: '',
    date_from: '',
    date_to: '',
    number_of_students: '',
    number_of_faculty: '',
    outcome: '',
    report_link: '',
  });

  const [file, setFile] = useState(null);

  const toast = useToast();

  const handleInputChange = useCallback((event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  }, []);

  const handleFileChange = useCallback((event) => {
    setFile(event.target.files[0]);
  }, []);

  const handleSubmit = useCallback(async (event) => {
    event.preventDefault();

    // Create a FormData object
    const formDataToSubmit = new FormData();
    formDataToSubmit.append('place_of_visit', formData.place_of_visit);
    formDataToSubmit.append('date_from', formData.date_from);
    formDataToSubmit.append('date_to', formData.date_to);
    formDataToSubmit.append('number_of_students', formData.number_of_students);
    formDataToSubmit.append('number_of_faculty', formData.number_of_faculty);
    formDataToSubmit.append('outcome', formData.outcome);
    formDataToSubmit.append('report_link', formData.report_link);

    if (file) {
      formDataToSubmit.append('proof', file);
    }

    try {
      const response = await axios.post(
        'http://localhost:8000/api/industrial-visits/',
        formDataToSubmit,
        {
          headers: {
            'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNDc5NjYyLCJpYXQiOjE3MjM0NzYwNjIsImp0aSI6ImNiM2VlOTVlZTM2MTQ2OGZiNThjYmMyYmFjNjdkY2EwIiwidXNlcl9pZCI6MX0.PmE8DVWfl7A-9NI9rfHiiDmi4RbSmOpvqKQcSMxfh-I`, // Replace with your actual token
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      console.log('Submitted Data:', response.data);
      toast({
        title: "Submission Successful",
        description: "Industrial visit data has been submitted.",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Error submitting data:', error);
      toast({
        title: "Submission Failed",
        description: "There was an error submitting the data. Please try again.",
        status: "error",
        duration: 5000,
        isClosable: true,
      });
    }
  }, [formData, file, toast]);

  const handleReset = useCallback(() => {
    setFormData({
      place_of_visit: '',
      date_from: '',
      date_to: '',
      number_of_students: '',
      number_of_faculty: '',
      outcome: '',
      report_link: '',
    });
    setFile(null);
  }, []);

  return (
    <>
      <Navbar/>
      <Flex direction="column" align="center" justify="center" py={2}>
        <Box p={8} rounded="md" w="full" maxW="700px">
          <Heading as="h3" size="lg" mb={6} textAlign="center">
            Industrial Visit
          </Heading>
          <hr />
          <br />
          <form onSubmit={handleSubmit}>
            <VStack spacing={6}>
              <HStack w="100%">
                <FormLabel htmlFor="place_of_visit" flex="1">
                  Place of Visit:
                </FormLabel>
                <Input
                  type="text"
                  id="place_of_visit"
                  name="place_of_visit"
                  value={formData.place_of_visit}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              <HStack w="100%">
                <FormLabel htmlFor="date_from" flex="1">
                  Date From:
                </FormLabel>
                <Input
                  type="date"
                  id="date_from"
                  name="date_from"
                  value={formData.date_from}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              <HStack w="100%">
                <FormLabel htmlFor="date_to" flex="1">
                  Date To:
                </FormLabel>
                <Input
                  type="date"
                  id="date_to"
                  name="date_to"
                  value={formData.date_to}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              <HStack w="100%">
                <FormLabel htmlFor="number_of_students" flex="1">
                  Number of Students:
                </FormLabel>
                <Input
                  type="number"
                  id="number_of_students"
                  name="number_of_students"
                  value={formData.number_of_students}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              <HStack w="100%">
                <FormLabel htmlFor="number_of_faculty" flex="1">
                  Number of Faculty:
                </FormLabel>
                <Input
                  type="text"
                  id="number_of_faculty"
                  name="number_of_faculty"
                  value={formData.number_of_faculty}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              <HStack w="100%">
                <FormLabel htmlFor="outcome" flex="1">
                  Outcome:
                </FormLabel>
                <Textarea
                  id="outcome"
                  name="outcome"
                  value={formData.outcome}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack>

              {/* <HStack w="100%">
                <FormLabel htmlFor="report_link" flex="1">
                  Report Link:
                </FormLabel>
                <Input
                  type="url"
                  id="report_link"
                  name="report_link"
                  value={formData.report_link}
                  onChange={handleInputChange}
                  flex="2"
                />
              </HStack> */}

              <HStack w="100%">
                <FormLabel htmlFor="proof" flex="1">
                  Proof:
                </FormLabel>
                <Input
                  type="file"
                  id="proof"
                  name="proof"
                  onChange={handleFileChange}
                  flex="2"
                />
              </HStack>

              <HStack spacing={4} pt={4}>
                <Button type="submit">
                  Submit
                </Button>
                <Button variant="outline" colorScheme="red" onClick={handleReset}>
                  Reset
                </Button>
              </HStack>
            </VStack>
          </form>
        </Box>
      </Flex>
    </>
  );
};

export default IndustrialVisitForm;
