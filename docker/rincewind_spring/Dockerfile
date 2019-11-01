## First phase
FROM maven:3.6.0-jdk-11 AS build
# Creating app directory
WORKDIR /usr/src/app
# Copying Application
COPY spring ./
# Getting .m2 libraries
RUN mvn clean package


## Second Phase
FROM openjdk:11  
# Copying Jar
COPY --from=build /usr/src/app/target/spring-1.0-SNAPSHOT.jar /usr/app/spring-1.0-SNAPSHOT.jar
# Exposing Port
EXPOSE 8080
# Running App
ENTRYPOINT ["java","-jar","/usr/app/spring-1.0-SNAPSHOT.jar"]  
