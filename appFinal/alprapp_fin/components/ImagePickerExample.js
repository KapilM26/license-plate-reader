import React, { useState, useEffect } from "react";
import {
  Modal,
  Text,
  TouchableOpacity,
  View,
  Image,
  Platform,
  ScrollView,
  Picker,
  Linking,
} from "react-native";
import { Camera } from "expo-camera";
import { Button,TextInput } from "react-native-paper";
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import { sendEmail } from './sendEmail';
import qs from 'qs';

import axios from 'axios';

const CameraModule = (props) => {
   const [cameraRef, setCameraRef] = useState(null);
   const [type, setType] = useState(Camera.Constants.Type.back);
return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={true}
      onRequestClose={() => {
        props.setModalVisible();
      }}
    >
      <Camera
        style={{ flex: 1 }}
        ratio="16:9"
        flashMode={Camera.Constants.FlashMode.auto}
        type={type}
        ref={(ref) => {
          setCameraRef(ref);
        }}
      >
        <View
          style={{
            flex: 1,
            backgroundColor: "transparent",
            justifyContent: "flex-end",
          }}
        >
          <View
            style={{
              backgroundColor: "black",
              flexDirection: "row",
              alignItems: "center",
              justifyContent: "space-between",
            }}
          >
            <Button
              style={{ marginLeft: 12 }}
              mode="outlined"
              color="white"
              onPress={() => {
              props.setModalVisible();
              }}
            >
              Close
            </Button>
           <TouchableOpacity
              onPress={async () => {
                if (cameraRef) {
                  let photo = await cameraRef.takePictureAsync();
                  props.setImage(photo);
                  props.setModalVisible();
                  }
              }}
            >
              <View
                style={{
                  borderWidth: 2,
                  borderRadius: 50,
                  borderColor: "white",
                  height: 50,
                  width: 50,
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  marginBottom: 16,
                  marginTop: 16,
                }}
              >
                <View
                  style={{
                    borderWidth: 2,
                    borderRadius: 50,
                    borderColor: "white",
                    height: 40,
                    width: 40,
                    backgroundColor: "white",
                  }}
                ></View>
              </View>
            </TouchableOpacity>
       <Button
              style={{ marginRight: 12 }}
              mode="outlined"
              color="white"
              onPress={() => {
                setType(
                  type === Camera.Constants.Type.back
                    ? Camera.Constants.Type.front
                    : Camera.Constants.Type.back
                );
              }}
            >
           {type === Camera.Constants.Type.back ? "Front" : "Back "}
            </Button>
        
          </View>
        </View>
      </Camera>
    </Modal>
  );
};
export default function ImagePickerExample() {
  const [selectedValue, setSelectedValue] = useState("Select");
  const [text, setText] = useState('');
  const [image, setImage] = useState(null);
  const [camera, setShowCamera] = useState(false);
  const [hasPermission, setHasPermission] = useState(null);
 useEffect(() => {
    (async () => {
       if (Platform.OS === 'ios') {
      const { status } = await Permissions.askAsync(Permissions.CAMERA_ROLL);
      if (status !== 'granted') {
        alert('Sorry, we need camera roll permissions to make this work!');
      }
    }
    // Camera Permission
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasPermission: status === 'granted' });
    })();
  }, []);
   const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    console.log(result);

    if (!result.cancelled) {
      setImage(result.uri);
    }
   
    

   };
  
return (
  <ScrollView>
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center", marginTop: 50 }}>
    <Text style={{fontSize: 30, marginTop: 10, marginBottom: 15 }}>
          ALPR APP
        </Text>
      <View
        style={{
          backgroundColor: "#eeee",
          width: 120,
          height: 120,
          borderRadius: 100,
          marginBottom: 8,
        }}
      >
        <Image
          source={{ uri: image }}
          style={{ width: 120, height: 120, borderRadius: 10 }}
        />
      </View>
      <Button
        style={{ width: "60%", marginTop: 16 }}
        mode="contained"
        onPress={() => {
          setShowCamera(true);
        }}
      >
        Camera
      </Button>
    {camera && (
        <CameraModule
          showModal={camera}
          setModalVisible={() => setShowCamera(false)}
          setImage={(result) => setImage(result.uri)}
        />
      )}
       <Button
        style={{ width: "60%", marginTop: 16 }}
        mode="contained"
        onPress={pickImage}
      >
        Select Image
      </Button>
       <Button
        style={{ width: "60%", marginTop: 16 }}
        mode="contained"
         onPress={() => {
           //axios.post("")
           //then(setShowCamera(false));
           setShowCamera(false);
        }}
      >
        Process Image
                
      </Button>
      <Text style={{fontSize: 17, marginTop: 30 }}>
         
         Owner Details
        </Text>
            <TextInput
        style={{height: 200,width:200,marginTop: 20, padding:5, textAlignVertical: 'top'}}
        onChangeText={text => setText(text)}
        defaultValue={text}
      />
      <Text style={{padding: 10, fontSize: 42}}>
        {text.split(' ').map((word) => word && ' ').join(' ')}
      </Text>
      <Text style={{fontSize: 17, marginTop: -40, marginBottom: 5 }}>
          Offence Registered
        </Text>
      <Picker
        selectedValue={selectedValue}
        style={{ height: 50, width: 200 }}
        onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
      >
        <Picker.Item label="Select" value="Select" />
        <Picker.Item label="Overspeeding" value="Overspeeding" />
        <Picker.Item label="Standing beyond zebra crossing" value="Standing beyond zebra crossing" />
        <Picker.Item label="Not wearing seat belt" value="Not wearing seat belt" />
        <Picker.Item label="License missing " value="License missing " />
        <Picker.Item label="RC invalid/missing" value="RC invalid/missing" />
        <Picker.Item label="Insurance invalid/missing" value="Insurance invalid/missing" />
        <Picker.Item label="PUC invalid/missing" value="PUC invalid/missing" />
        <Picker.Item label="Vehicle Fitness not renewed" value="Vehicle Fitness not renewed" />
        <Picker.Item label="Non obeyance of Traffic Signal" value="Non obeyance of Traffic Signal" />
        <Picker.Item label="Not wearing Seat Belt" value="Not wearing Seat Belt" />
        <Picker.Item label="Drink and Drive" value="Drink and Drive" />
      </Picker>
      //Email button working
       <Button
        style={{ width: "60%", marginTop: 16, marginBottom:30 }}
        mode="contained"
         onPress={() => {sendEmail(
    'shgodbole2799@gmail.com',                  //add the string for owners email from database
    'Offence Registered!!',
    'Your vehicle has been charged for '+selectedValue+ '.The fine to be paid is xx rupees. ',
).then(() => {
    console.log('Our email successfully provided to device mail ');
          
        });}}
      >
       Send Email
      </Button>
    </View>
    </ScrollView>
  );
   }