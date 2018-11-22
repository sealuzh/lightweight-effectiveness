/*
 *  Copyright 2001-present Stephen Colebourne
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package org.joda.beans.sample;

import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

import org.joda.beans.Bean;
import org.joda.beans.ImmutableBean;
import org.joda.beans.JodaBeanUtils;
import org.joda.beans.MetaBean;
import org.joda.beans.MetaProperty;
import org.joda.beans.gen.BeanDefinition;
import org.joda.beans.gen.PropertyDefinition;
import org.joda.beans.impl.direct.DirectFieldsBeanBuilder;
import org.joda.beans.impl.direct.DirectMetaBean;
import org.joda.beans.impl.direct.DirectMetaProperty;
import org.joda.beans.impl.direct.DirectMetaPropertyMap;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;

/**
 * Mock JavaBean, used for testing.
 * 
 * @author Stephen Colebourne
 */
@BeanDefinition(builderScope = "public", factoryName = "of")
public final class ImmTypes<T extends Comparable<T>> implements ImmutableBean {

    @PropertyDefinition(validate = "notNull")
    private final ImmutableList<?> listWild;
    @PropertyDefinition(validate = "notNull", type = "List<?>")
    private final List<Object> listWildPublic1;
    @PropertyDefinition(validate = "notNull", type = "ImmutableList<?>")
    private final ImmutableList<Object> listWildPublic2;

    @PropertyDefinition(validate = "notNull", builderType = "List<?>")
    private final List<Object> listWildBuilder1;
    @PropertyDefinition(validate = "notNull", builderType = "List<? extends Address>")
    private final List<Address> listWildBuilder2;
    @PropertyDefinition(validate = "notNull", builderType = "Map<String, ? extends Address>")
    private final Map<String, Address> mapWildBuilder1;

    //------------------------- AUTOGENERATED START -------------------------
    /**
     * The meta-bean for {@code ImmTypes}.
     * @return the meta-bean, not null
     */
    @SuppressWarnings("rawtypes")
    public static ImmTypes.Meta meta() {
        return ImmTypes.Meta.INSTANCE;
    }

    /**
     * The meta-bean for {@code ImmTypes}.
     * @param <R>  the bean's generic type
     * @param cls  the bean's generic type
     * @return the meta-bean, not null
     */
    @SuppressWarnings("unchecked")
    public static <R extends Comparable<R>> ImmTypes.Meta<R> metaImmTypes(Class<R> cls) {
        return ImmTypes.Meta.INSTANCE;
    }

    static {
        MetaBean.register(ImmTypes.Meta.INSTANCE);
    }

    /**
     * Obtains an instance.
     * @param <T>  the type
     * @param listWild  the value of the property, not null
     * @param listWildPublic1  the value of the property, not null
     * @param listWildPublic2  the value of the property, not null
     * @param listWildBuilder1  the value of the property, not null
     * @param listWildBuilder2  the value of the property, not null
     * @param mapWildBuilder1  the value of the property, not null
     * @return the instance
     */
    public static <T extends Comparable<T>> ImmTypes<T> of(
            List<?> listWild,
            List<?> listWildPublic1,
            List<?> listWildPublic2,
            List<?> listWildBuilder1,
            List<? extends Address> listWildBuilder2,
            Map<String, ? extends Address> mapWildBuilder1) {
        return new ImmTypes<>(
            listWild,
            listWildPublic1,
            listWildPublic2,
            listWildBuilder1,
            listWildBuilder2,
            mapWildBuilder1);
    }

    /**
     * Returns a builder used to create an instance of the bean.
     * @param <T>  the type
     * @return the builder, not null
     */
    public static <T extends Comparable<T>> ImmTypes.Builder<T> builder() {
        return new ImmTypes.Builder<>();
    }

    private ImmTypes(
            List<?> listWild,
            List<?> listWildPublic1,
            List<?> listWildPublic2,
            List<?> listWildBuilder1,
            List<? extends Address> listWildBuilder2,
            Map<String, ? extends Address> mapWildBuilder1) {
        JodaBeanUtils.notNull(listWild, "listWild");
        JodaBeanUtils.notNull(listWildPublic1, "listWildPublic1");
        JodaBeanUtils.notNull(listWildPublic2, "listWildPublic2");
        JodaBeanUtils.notNull(listWildBuilder1, "listWildBuilder1");
        JodaBeanUtils.notNull(listWildBuilder2, "listWildBuilder2");
        JodaBeanUtils.notNull(mapWildBuilder1, "mapWildBuilder1");
        this.listWild = ImmutableList.copyOf(listWild);
        this.listWildPublic1 = ImmutableList.copyOf(listWildPublic1);
        this.listWildPublic2 = ImmutableList.copyOf(listWildPublic2);
        this.listWildBuilder1 = ImmutableList.copyOf(listWildBuilder1);
        this.listWildBuilder2 = ImmutableList.copyOf(listWildBuilder2);
        this.mapWildBuilder1 = ImmutableMap.copyOf(mapWildBuilder1);
    }

    @SuppressWarnings("unchecked")
    @Override
    public ImmTypes.Meta<T> metaBean() {
        return ImmTypes.Meta.INSTANCE;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the listWild.
     * @return the value of the property, not null
     */
    public ImmutableList<?> getListWild() {
        return listWild;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the listWildPublic1.
     * @return the value of the property, not null
     */
    public List<?> getListWildPublic1() {
        return listWildPublic1;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the listWildPublic2.
     * @return the value of the property, not null
     */
    public ImmutableList<?> getListWildPublic2() {
        return listWildPublic2;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the listWildBuilder1.
     * @return the value of the property, not null
     */
    public List<Object> getListWildBuilder1() {
        return listWildBuilder1;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the listWildBuilder2.
     * @return the value of the property, not null
     */
    public List<Address> getListWildBuilder2() {
        return listWildBuilder2;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the mapWildBuilder1.
     * @return the value of the property, not null
     */
    public Map<String, Address> getMapWildBuilder1() {
        return mapWildBuilder1;
    }

    //-----------------------------------------------------------------------
    /**
     * Returns a builder that allows this bean to be mutated.
     * @return the mutable builder, not null
     */
    public Builder<T> toBuilder() {
        return new Builder<>(this);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (obj != null && obj.getClass() == this.getClass()) {
            ImmTypes<?> other = (ImmTypes<?>) obj;
            return JodaBeanUtils.equal(listWild, other.listWild) &&
                    JodaBeanUtils.equal(listWildPublic1, other.listWildPublic1) &&
                    JodaBeanUtils.equal(listWildPublic2, other.listWildPublic2) &&
                    JodaBeanUtils.equal(listWildBuilder1, other.listWildBuilder1) &&
                    JodaBeanUtils.equal(listWildBuilder2, other.listWildBuilder2) &&
                    JodaBeanUtils.equal(mapWildBuilder1, other.mapWildBuilder1);
        }
        return false;
    }

    @Override
    public int hashCode() {
        int hash = getClass().hashCode();
        hash = hash * 31 + JodaBeanUtils.hashCode(listWild);
        hash = hash * 31 + JodaBeanUtils.hashCode(listWildPublic1);
        hash = hash * 31 + JodaBeanUtils.hashCode(listWildPublic2);
        hash = hash * 31 + JodaBeanUtils.hashCode(listWildBuilder1);
        hash = hash * 31 + JodaBeanUtils.hashCode(listWildBuilder2);
        hash = hash * 31 + JodaBeanUtils.hashCode(mapWildBuilder1);
        return hash;
    }

    @Override
    public String toString() {
        StringBuilder buf = new StringBuilder(224);
        buf.append("ImmTypes{");
        buf.append("listWild").append('=').append(listWild).append(',').append(' ');
        buf.append("listWildPublic1").append('=').append(listWildPublic1).append(',').append(' ');
        buf.append("listWildPublic2").append('=').append(listWildPublic2).append(',').append(' ');
        buf.append("listWildBuilder1").append('=').append(listWildBuilder1).append(',').append(' ');
        buf.append("listWildBuilder2").append('=').append(listWildBuilder2).append(',').append(' ');
        buf.append("mapWildBuilder1").append('=').append(JodaBeanUtils.toString(mapWildBuilder1));
        buf.append('}');
        return buf.toString();
    }

    //-----------------------------------------------------------------------
    /**
     * The meta-bean for {@code ImmTypes}.
     * @param <T>  the type
     */
    public static final class Meta<T extends Comparable<T>> extends DirectMetaBean {
        /**
         * The singleton instance of the meta-bean.
         */
        @SuppressWarnings("rawtypes")
        static final Meta INSTANCE = new Meta();

        /**
         * The meta-property for the {@code listWild} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<ImmutableList<?>> listWild = DirectMetaProperty.ofImmutable(
                this, "listWild", ImmTypes.class, (Class) ImmutableList.class);
        /**
         * The meta-property for the {@code listWildPublic1} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<List<?>> listWildPublic1 = DirectMetaProperty.ofImmutable(
                this, "listWildPublic1", ImmTypes.class, (Class) List.class);
        /**
         * The meta-property for the {@code listWildPublic2} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<ImmutableList<?>> listWildPublic2 = DirectMetaProperty.ofImmutable(
                this, "listWildPublic2", ImmTypes.class, (Class) ImmutableList.class);
        /**
         * The meta-property for the {@code listWildBuilder1} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<List<Object>> listWildBuilder1 = DirectMetaProperty.ofImmutable(
                this, "listWildBuilder1", ImmTypes.class, (Class) List.class);
        /**
         * The meta-property for the {@code listWildBuilder2} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<List<Address>> listWildBuilder2 = DirectMetaProperty.ofImmutable(
                this, "listWildBuilder2", ImmTypes.class, (Class) List.class);
        /**
         * The meta-property for the {@code mapWildBuilder1} property.
         */
        @SuppressWarnings({"unchecked", "rawtypes" })
        private final MetaProperty<Map<String, Address>> mapWildBuilder1 = DirectMetaProperty.ofImmutable(
                this, "mapWildBuilder1", ImmTypes.class, (Class) Map.class);
        /**
         * The meta-properties.
         */
        private final Map<String, MetaProperty<?>> metaPropertyMap$ = new DirectMetaPropertyMap(
                this, null,
                "listWild",
                "listWildPublic1",
                "listWildPublic2",
                "listWildBuilder1",
                "listWildBuilder2",
                "mapWildBuilder1");

        /**
         * Restricted constructor.
         */
        private Meta() {
        }

        @Override
        protected MetaProperty<?> metaPropertyGet(String propertyName) {
            switch (propertyName.hashCode()) {
                case 1345738120:  // listWild
                    return listWild;
                case 1874924608:  // listWildPublic1
                    return listWildPublic1;
                case 1874924609:  // listWildPublic2
                    return listWildPublic2;
                case -436161122:  // listWildBuilder1
                    return listWildBuilder1;
                case -436161121:  // listWildBuilder2
                    return listWildBuilder2;
                case -2009039524:  // mapWildBuilder1
                    return mapWildBuilder1;
            }
            return super.metaPropertyGet(propertyName);
        }

        @Override
        public ImmTypes.Builder<T> builder() {
            return new ImmTypes.Builder<>();
        }

        @SuppressWarnings({"unchecked", "rawtypes" })
        @Override
        public Class<? extends ImmTypes<T>> beanType() {
            return (Class) ImmTypes.class;
        }

        @Override
        public Map<String, MetaProperty<?>> metaPropertyMap() {
            return metaPropertyMap$;
        }

        //-----------------------------------------------------------------------
        /**
         * The meta-property for the {@code listWild} property.
         * @return the meta-property, not null
         */
        public MetaProperty<ImmutableList<?>> listWild() {
            return listWild;
        }

        /**
         * The meta-property for the {@code listWildPublic1} property.
         * @return the meta-property, not null
         */
        public MetaProperty<List<?>> listWildPublic1() {
            return listWildPublic1;
        }

        /**
         * The meta-property for the {@code listWildPublic2} property.
         * @return the meta-property, not null
         */
        public MetaProperty<ImmutableList<?>> listWildPublic2() {
            return listWildPublic2;
        }

        /**
         * The meta-property for the {@code listWildBuilder1} property.
         * @return the meta-property, not null
         */
        public MetaProperty<List<Object>> listWildBuilder1() {
            return listWildBuilder1;
        }

        /**
         * The meta-property for the {@code listWildBuilder2} property.
         * @return the meta-property, not null
         */
        public MetaProperty<List<Address>> listWildBuilder2() {
            return listWildBuilder2;
        }

        /**
         * The meta-property for the {@code mapWildBuilder1} property.
         * @return the meta-property, not null
         */
        public MetaProperty<Map<String, Address>> mapWildBuilder1() {
            return mapWildBuilder1;
        }

        //-----------------------------------------------------------------------
        @Override
        protected Object propertyGet(Bean bean, String propertyName, boolean quiet) {
            switch (propertyName.hashCode()) {
                case 1345738120:  // listWild
                    return ((ImmTypes<?>) bean).getListWild();
                case 1874924608:  // listWildPublic1
                    return ((ImmTypes<?>) bean).getListWildPublic1();
                case 1874924609:  // listWildPublic2
                    return ((ImmTypes<?>) bean).getListWildPublic2();
                case -436161122:  // listWildBuilder1
                    return ((ImmTypes<?>) bean).getListWildBuilder1();
                case -436161121:  // listWildBuilder2
                    return ((ImmTypes<?>) bean).getListWildBuilder2();
                case -2009039524:  // mapWildBuilder1
                    return ((ImmTypes<?>) bean).getMapWildBuilder1();
            }
            return super.propertyGet(bean, propertyName, quiet);
        }

        @Override
        protected void propertySet(Bean bean, String propertyName, Object newValue, boolean quiet) {
            metaProperty(propertyName);
            if (quiet) {
                return;
            }
            throw new UnsupportedOperationException("Property cannot be written: " + propertyName);
        }

    }

    //-----------------------------------------------------------------------
    /**
     * The bean-builder for {@code ImmTypes}.
     * @param <T>  the type
     */
    public static final class Builder<T extends Comparable<T>> extends DirectFieldsBeanBuilder<ImmTypes<T>> {

        private List<?> listWild = ImmutableList.of();
        private List<?> listWildPublic1 = ImmutableList.of();
        private List<?> listWildPublic2 = ImmutableList.of();
        private List<?> listWildBuilder1 = ImmutableList.of();
        private List<? extends Address> listWildBuilder2 = ImmutableList.of();
        private Map<String, ? extends Address> mapWildBuilder1 = ImmutableMap.of();

        /**
         * Restricted constructor.
         */
        private Builder() {
        }

        /**
         * Restricted copy constructor.
         * @param beanToCopy  the bean to copy from, not null
         */
        private Builder(ImmTypes<T> beanToCopy) {
            this.listWild = beanToCopy.getListWild();
            this.listWildPublic1 = ImmutableList.copyOf(beanToCopy.getListWildPublic1());
            this.listWildPublic2 = beanToCopy.getListWildPublic2();
            this.listWildBuilder1 = ImmutableList.copyOf(beanToCopy.getListWildBuilder1());
            this.listWildBuilder2 = ImmutableList.copyOf(beanToCopy.getListWildBuilder2());
            this.mapWildBuilder1 = ImmutableMap.copyOf(beanToCopy.getMapWildBuilder1());
        }

        //-----------------------------------------------------------------------
        @Override
        public Object get(String propertyName) {
            switch (propertyName.hashCode()) {
                case 1345738120:  // listWild
                    return listWild;
                case 1874924608:  // listWildPublic1
                    return listWildPublic1;
                case 1874924609:  // listWildPublic2
                    return listWildPublic2;
                case -436161122:  // listWildBuilder1
                    return listWildBuilder1;
                case -436161121:  // listWildBuilder2
                    return listWildBuilder2;
                case -2009039524:  // mapWildBuilder1
                    return mapWildBuilder1;
                default:
                    throw new NoSuchElementException("Unknown property: " + propertyName);
            }
        }

        @SuppressWarnings("unchecked")
        @Override
        public Builder<T> set(String propertyName, Object newValue) {
            switch (propertyName.hashCode()) {
                case 1345738120:  // listWild
                    this.listWild = (List<?>) newValue;
                    break;
                case 1874924608:  // listWildPublic1
                    this.listWildPublic1 = (List<?>) newValue;
                    break;
                case 1874924609:  // listWildPublic2
                    this.listWildPublic2 = (List<?>) newValue;
                    break;
                case -436161122:  // listWildBuilder1
                    this.listWildBuilder1 = (List<?>) newValue;
                    break;
                case -436161121:  // listWildBuilder2
                    this.listWildBuilder2 = (List<? extends Address>) newValue;
                    break;
                case -2009039524:  // mapWildBuilder1
                    this.mapWildBuilder1 = (Map<String, ? extends Address>) newValue;
                    break;
                default:
                    throw new NoSuchElementException("Unknown property: " + propertyName);
            }
            return this;
        }

        @Override
        public Builder<T> set(MetaProperty<?> property, Object value) {
            super.set(property, value);
            return this;
        }

        @Override
        public ImmTypes<T> build() {
            return new ImmTypes<>(
                    listWild,
                    listWildPublic1,
                    listWildPublic2,
                    listWildBuilder1,
                    listWildBuilder2,
                    mapWildBuilder1);
        }

        //-----------------------------------------------------------------------
        /**
         * Sets the listWild.
         * @param listWild  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWild(List<?> listWild) {
            JodaBeanUtils.notNull(listWild, "listWild");
            this.listWild = listWild;
            return this;
        }

        /**
         * Sets the {@code listWild} property in the builder
         * from an array of objects.
         * @param listWild  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWild(Object... listWild) {
            return listWild(ImmutableList.copyOf(listWild));
        }

        /**
         * Sets the listWildPublic1.
         * @param listWildPublic1  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildPublic1(List<?> listWildPublic1) {
            JodaBeanUtils.notNull(listWildPublic1, "listWildPublic1");
            this.listWildPublic1 = listWildPublic1;
            return this;
        }

        /**
         * Sets the {@code listWildPublic1} property in the builder
         * from an array of objects.
         * @param listWildPublic1  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildPublic1(Object... listWildPublic1) {
            return listWildPublic1(ImmutableList.copyOf(listWildPublic1));
        }

        /**
         * Sets the listWildPublic2.
         * @param listWildPublic2  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildPublic2(List<?> listWildPublic2) {
            JodaBeanUtils.notNull(listWildPublic2, "listWildPublic2");
            this.listWildPublic2 = listWildPublic2;
            return this;
        }

        /**
         * Sets the {@code listWildPublic2} property in the builder
         * from an array of objects.
         * @param listWildPublic2  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildPublic2(Object... listWildPublic2) {
            return listWildPublic2(ImmutableList.copyOf(listWildPublic2));
        }

        /**
         * Sets the listWildBuilder1.
         * @param listWildBuilder1  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildBuilder1(List<?> listWildBuilder1) {
            JodaBeanUtils.notNull(listWildBuilder1, "listWildBuilder1");
            this.listWildBuilder1 = listWildBuilder1;
            return this;
        }

        /**
         * Sets the {@code listWildBuilder1} property in the builder
         * from an array of objects.
         * @param listWildBuilder1  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildBuilder1(Object... listWildBuilder1) {
            return listWildBuilder1(ImmutableList.copyOf(listWildBuilder1));
        }

        /**
         * Sets the listWildBuilder2.
         * @param listWildBuilder2  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildBuilder2(List<? extends Address> listWildBuilder2) {
            JodaBeanUtils.notNull(listWildBuilder2, "listWildBuilder2");
            this.listWildBuilder2 = listWildBuilder2;
            return this;
        }

        /**
         * Sets the {@code listWildBuilder2} property in the builder
         * from an array of objects.
         * @param listWildBuilder2  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> listWildBuilder2(Address... listWildBuilder2) {
            return listWildBuilder2(ImmutableList.copyOf(listWildBuilder2));
        }

        /**
         * Sets the mapWildBuilder1.
         * @param mapWildBuilder1  the new value, not null
         * @return this, for chaining, not null
         */
        public Builder<T> mapWildBuilder1(Map<String, ? extends Address> mapWildBuilder1) {
            JodaBeanUtils.notNull(mapWildBuilder1, "mapWildBuilder1");
            this.mapWildBuilder1 = mapWildBuilder1;
            return this;
        }

        //-----------------------------------------------------------------------
        @Override
        public String toString() {
            StringBuilder buf = new StringBuilder(224);
            buf.append("ImmTypes.Builder{");
            buf.append("listWild").append('=').append(JodaBeanUtils.toString(listWild)).append(',').append(' ');
            buf.append("listWildPublic1").append('=').append(JodaBeanUtils.toString(listWildPublic1)).append(',').append(' ');
            buf.append("listWildPublic2").append('=').append(JodaBeanUtils.toString(listWildPublic2)).append(',').append(' ');
            buf.append("listWildBuilder1").append('=').append(JodaBeanUtils.toString(listWildBuilder1)).append(',').append(' ');
            buf.append("listWildBuilder2").append('=').append(JodaBeanUtils.toString(listWildBuilder2)).append(',').append(' ');
            buf.append("mapWildBuilder1").append('=').append(JodaBeanUtils.toString(mapWildBuilder1));
            buf.append('}');
            return buf.toString();
        }

    }

    //-------------------------- AUTOGENERATED END --------------------------
}
