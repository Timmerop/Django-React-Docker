# Use an official node runtime as a parent image
FROM node:10
RUN mkdir /app
WORKDIR /app/
ENV PATH /app/node_modules/.bin:$PATH
# Install dependencies
COPY ./react_app/package*.json /app/
#RUN npm install
RUN npm install --silent
RUN npm install react-scripts@2.1.3 -g --silent

# Add rest of the client code
#COPY . /app/
#EXPOSE 3000
COPY ./react_app/* /app/
CMD ["npm", "start"]