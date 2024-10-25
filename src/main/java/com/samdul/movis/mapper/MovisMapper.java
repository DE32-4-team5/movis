package com.samdul.movis.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.samdul.movis.entity.MovisEntity;

@Mapper
public interface MovisMapper {
    MovisEntity findByNm(String nm);
    MovisEntity findByGn(String gn);
    MovisEntity findByPn(String pn);
}
