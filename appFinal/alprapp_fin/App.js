import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import Constants from 'expo-constants';

// You can import from local files
import ImagePickerExample from './components/ImagePickerExample';

// or any pure javascript modules available in npm
import axios from axios;

import { Card } from 'react-native-paper';

export default function App() {
  return (
    <View style={styles.container}>
      
      <Card>
        <ImagePickerExample />
      </Card>
    </View>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
});
