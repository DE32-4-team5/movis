package com.samdul.movis.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.samdul.movis.entity.MovisEntity;
import com.samdul.movis.mapper.MovisMapper;

@Service
public class MovisService {
    @Autowired
    MovisMapper movisMapper;

    public MovisEntity findByNm(String nm) {
        System.out.println("[service] selectOne");
        MovisEntity todo = movisMapper.findByNm(nm);
        return todo;
        
    }

    public MovisEntity findByGn(String gn) {
        System.out.println("[service] selectOne");
        MovisEntity todo = movisMapper.findByGn(gn);
        return todo;
        
    }

    public MovisEntity findByPn(String pn) {
        System.out.println("[service] selectOne");
        MovisEntity todo = movisMapper.findByPn(pn);
        return todo;
        
    }
}
