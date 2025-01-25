import React, { useState, useCallback } from "react";
import axios from "axios";
import {
  Flex,
  FormLabel,
  Select,
  Input,
  Button,
  Box,
  Heading,
  VStack,
  HStack,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
} from "@chakra-ui/react";
import Navbar from "../Component/navigationbar";

const StartupForm = () => {
  const [formFields, setFormFields] = useState({
    title: "",
    status: "",
  });
  const [students, setStudents] = useState([""]);
  const [faculty, setFaculty] = useState([{ id: "", verified: false }]);
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [modalType, setModalType] = useState("");
  const [modalInput, setModalInput] = useState("");
  const [token, setToken] = useState(""); // For storing JWT

  const handleSubmit = useCallback(
    async (event) => {
      event.preventDefault();
      const staticData = {
        team_members: "John Doe, Jane Smith, Dr. Robert Johnson",
        startup_name: "TechInnovate",
        status: "Active"
      };
      const data = { ...formFields, students, faculty, ...staticData };

      try {
        const response = await axios.post(
          "http://localhost:8000/api/startups/", // Your backend endpoint
          data,
          {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyOTcyMDY4LCJpYXQiOjE3MjI5Njg0NjgsImp0aSI6IjQyYTYzMDMzMDVmYzQzMTU5YjNiZjBiYmU5YTA4ZTdhIiwidXNlcl9pZCI6MX0.PwcdQcu7J00759l2EVqeIfgvf7CvU3A1MC2QpG8umH0`,
            },
          }
        );
        console.log("Submitted Data:", response.data);
      } catch (error) {
        console.error("Error submitting form:", error.response?.data || error.message);
      }
    },
    [formFields, students, faculty, token]
  );

  const handleReset = useCallback(() => {
    setFormFields({
      title: "",
      status: "",
    });
    setStudents([""]);
    setFaculty([{ id: "", verified: false }]);
    setModalInput("");
  }, []);

  const handleInputChange = useCallback((event) => {
    const { name, value } = event.target;
    setFormFields((prevFields) => ({ ...prevFields, [name]: value }));
  }, []);

  const handleChangeEntry = (type, index, value) => {
    if (type === "student") {
      setStudents((prev) =>
        prev.map((item, idx) => (idx === index ? value : item))
      );
    } else if (type === "faculty") {
      setFaculty((prev) =>
        prev.map((item, idx) => (idx === index ? { ...item, id: value } : item))
      );
    }
  };

  const handleVerify = (index) => {
    setFaculty((prev) =>
      prev.map((item, idx) =>
        idx === index ? { ...item, verified: true } : item
      )
    );
  };

  const handleOpenModal = (type) => {
    setModalType(type);
    setModalInput("");
    onOpen();
  };

  const handleAddEntry = (type) => {
    if (type === "student") {
      setStudents((prev) => [...prev, ""]);
    } else if (type === "faculty") {
      setFaculty((prev) => [...prev, { id: "", verified: false }]);
    }
    onClose();
  };

  return (
    <>
    <Navbar/>
      <Flex
        direction="column"
        align="center"
        justify="center"
        bg="gray.50"
        p={4}
      >
        <Heading as="h3" size="lg" my={5} textAlign="center">
          Startups
        </Heading>
        <form onSubmit={handleSubmit}>
          <VStack spacing={4}>
            <HStack w="100%" align="start" spacing={4}>
              <FormLabel htmlFor="students" flex="1">
                Students:
              </FormLabel>
              <Box flex="3">
                {students.map((student, index) => (
                  <HStack key={index} mb={2}>
                    <Input
                      type="text"
                      value={student}
                      placeholder="Add student"
                      onChange={(e) =>
                        handleChangeEntry("student", index, e.target.value)
                      }
                    />
                    {index === students.length - 1 && (
                      <Button
                        variant="ghost"
                        colorScheme="blue"
                        type="button"
                        p={0}
                        minW={8}
                        h={8}
                        onClick={() => handleAddEntry("student")}
                      >
                        +
                      </Button>
                    )}
                  </HStack>
                ))}
              </Box>
            </HStack>
            <HStack w="100%" align="start" spacing={4}>
              <FormLabel htmlFor="faculty" flex="1">
                Faculty:
              </FormLabel>
              <Box flex="3">
                {faculty.map((fac, index) => (
                  <HStack key={index} mb={2}>
                    <Input
                      type="text"
                      value={fac.id}
                      placeholder="Add faculty"
                      onChange={(e) =>
                        handleChangeEntry("faculty", index, e.target.value)
                      }
                    />
                    <Button
                      variant="ghost"
                      colorScheme="green"
                      type="button"
                      p={0}
                      minW={8}
                      h={8}
                      onClick={() => handleVerify(index)}
                      isDisabled={fac.verified}
                    >
                      {fac.verified ? "Verified" : "Verify"}
                    </Button>
                    {index === faculty.length - 1 && (
                      <Button
                        variant="ghost"
                        colorScheme="blue"
                        type="button"
                        p={0}
                        minW={8}
                        h={8}
                        onClick={() => handleAddEntry("faculty")}
                      >
                        +
                      </Button>
                    )}
                  </HStack>
                ))}
              </Box>
            </HStack>
            <HStack w="100%">
              <FormLabel htmlFor="title" flex="1">
                Name of the Startup:
              </FormLabel>
              <Input
                type="text"
                id="title"
                name="title"
                value={formFields.title}
                onChange={handleInputChange}
                flex="3"
              />
            </HStack>
            <HStack w="100%">
              <FormLabel htmlFor="status" flex="1">
                Status:
              </FormLabel>
              <Select
                id="status"
                name="status"
                placeholder="Select status"
                value={formFields.status}
                onChange={handleInputChange}
                flex="3"
              >
                <option value="pre-incubation">Pre-Incubation</option>
                <option value="incubation">Incubation</option>
                <option value="granted">Granted</option>
              </Select>
            </HStack>
            <HStack spacing={4} pt={4}>
              <Button type="submit">Submit</Button>
              <Button variant="outline" colorScheme="red" onClick={handleReset}>
                Reset
              </Button>
            </HStack>
          </VStack>
        </form>

        <Modal isOpen={isOpen} onClose={onClose}>
          <ModalOverlay />
          <ModalContent>
            <ModalHeader>Add {modalType}</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <Input
                placeholder={`Enter ${modalType} name`}
                value={modalInput}
                onChange={(e) => setModalInput(e.target.value)}
              />
            </ModalBody>
            <ModalFooter>
              <Button
                colorScheme="blue"
                mr={3}
                onClick={() => handleAddEntry(modalType)}
              >
                Add
              </Button>
              <Button variant="ghost" onClick={onClose}>
                Close
              </Button>
            </ModalFooter>
          </ModalContent>
        </Modal>
      </Flex>
    </>
  );
};

export default StartupForm;
