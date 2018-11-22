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

/**
 * Mock bean for primitive array testing.
 * 
 * @author Stephen Colebourne
 */
@BeanDefinition(factoryName = "of")
public final class ImmArrays implements ImmutableBean {

    @PropertyDefinition
    private final int[] intArray;
    @PropertyDefinition
    private final long[] longArray;
    @PropertyDefinition
    private final double[] doubleArray;
    @PropertyDefinition
    private final boolean[] booleanArray;

    //------------------------- AUTOGENERATED START -------------------------
    /**
     * The meta-bean for {@code ImmArrays}.
     * @return the meta-bean, not null
     */
    public static ImmArrays.Meta meta() {
        return ImmArrays.Meta.INSTANCE;
    }

    static {
        MetaBean.register(ImmArrays.Meta.INSTANCE);
    }

    /**
     * Obtains an instance.
     * @param intArray  the value of the property
     * @param longArray  the value of the property
     * @param doubleArray  the value of the property
     * @param booleanArray  the value of the property
     * @return the instance
     */
    public static ImmArrays of(
            int[] intArray,
            long[] longArray,
            double[] doubleArray,
            boolean[] booleanArray) {
        return new ImmArrays(
            intArray,
            longArray,
            doubleArray,
            booleanArray);
    }

    /**
     * Returns a builder used to create an instance of the bean.
     * @return the builder, not null
     */
    public static ImmArrays.Builder builder() {
        return new ImmArrays.Builder();
    }

    private ImmArrays(
            int[] intArray,
            long[] longArray,
            double[] doubleArray,
            boolean[] booleanArray) {
        this.intArray = (intArray != null ? intArray.clone() : null);
        this.longArray = (longArray != null ? longArray.clone() : null);
        this.doubleArray = (doubleArray != null ? doubleArray.clone() : null);
        this.booleanArray = booleanArray;
    }

    @Override
    public ImmArrays.Meta metaBean() {
        return ImmArrays.Meta.INSTANCE;
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the intArray.
     * @return the value of the property
     */
    public int[] getIntArray() {
        return (intArray != null ? intArray.clone() : null);
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the longArray.
     * @return the value of the property
     */
    public long[] getLongArray() {
        return (longArray != null ? longArray.clone() : null);
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the doubleArray.
     * @return the value of the property
     */
    public double[] getDoubleArray() {
        return (doubleArray != null ? doubleArray.clone() : null);
    }

    //-----------------------------------------------------------------------
    /**
     * Gets the booleanArray.
     * @return the value of the property
     */
    public boolean[] getBooleanArray() {
        return booleanArray;
    }

    //-----------------------------------------------------------------------
    /**
     * Returns a builder that allows this bean to be mutated.
     * @return the mutable builder, not null
     */
    public Builder toBuilder() {
        return new Builder(this);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (obj != null && obj.getClass() == this.getClass()) {
            ImmArrays other = (ImmArrays) obj;
            return JodaBeanUtils.equal(intArray, other.intArray) &&
                    JodaBeanUtils.equal(longArray, other.longArray) &&
                    JodaBeanUtils.equal(doubleArray, other.doubleArray) &&
                    JodaBeanUtils.equal(booleanArray, other.booleanArray);
        }
        return false;
    }

    @Override
    public int hashCode() {
        int hash = getClass().hashCode();
        hash = hash * 31 + JodaBeanUtils.hashCode(intArray);
        hash = hash * 31 + JodaBeanUtils.hashCode(longArray);
        hash = hash * 31 + JodaBeanUtils.hashCode(doubleArray);
        hash = hash * 31 + JodaBeanUtils.hashCode(booleanArray);
        return hash;
    }

    @Override
    public String toString() {
        StringBuilder buf = new StringBuilder(160);
        buf.append("ImmArrays{");
        buf.append("intArray").append('=').append(intArray).append(',').append(' ');
        buf.append("longArray").append('=').append(longArray).append(',').append(' ');
        buf.append("doubleArray").append('=').append(doubleArray).append(',').append(' ');
        buf.append("booleanArray").append('=').append(JodaBeanUtils.toString(booleanArray));
        buf.append('}');
        return buf.toString();
    }

    //-----------------------------------------------------------------------
    /**
     * The meta-bean for {@code ImmArrays}.
     */
    public static final class Meta extends DirectMetaBean {
        /**
         * The singleton instance of the meta-bean.
         */
        static final Meta INSTANCE = new Meta();

        /**
         * The meta-property for the {@code intArray} property.
         */
        private final MetaProperty<int[]> intArray = DirectMetaProperty.ofImmutable(
                this, "intArray", ImmArrays.class, int[].class);
        /**
         * The meta-property for the {@code longArray} property.
         */
        private final MetaProperty<long[]> longArray = DirectMetaProperty.ofImmutable(
                this, "longArray", ImmArrays.class, long[].class);
        /**
         * The meta-property for the {@code doubleArray} property.
         */
        private final MetaProperty<double[]> doubleArray = DirectMetaProperty.ofImmutable(
                this, "doubleArray", ImmArrays.class, double[].class);
        /**
         * The meta-property for the {@code booleanArray} property.
         */
        private final MetaProperty<boolean[]> booleanArray = DirectMetaProperty.ofImmutable(
                this, "booleanArray", ImmArrays.class, boolean[].class);
        /**
         * The meta-properties.
         */
        private final Map<String, MetaProperty<?>> metaPropertyMap$ = new DirectMetaPropertyMap(
                this, null,
                "intArray",
                "longArray",
                "doubleArray",
                "booleanArray");

        /**
         * Restricted constructor.
         */
        private Meta() {
        }

        @Override
        protected MetaProperty<?> metaPropertyGet(String propertyName) {
            switch (propertyName.hashCode()) {
                case 537167786:  // intArray
                    return intArray;
                case 100362557:  // longArray
                    return longArray;
                case -1645494008:  // doubleArray
                    return doubleArray;
                case -1066176751:  // booleanArray
                    return booleanArray;
            }
            return super.metaPropertyGet(propertyName);
        }

        @Override
        public ImmArrays.Builder builder() {
            return new ImmArrays.Builder();
        }

        @Override
        public Class<? extends ImmArrays> beanType() {
            return ImmArrays.class;
        }

        @Override
        public Map<String, MetaProperty<?>> metaPropertyMap() {
            return metaPropertyMap$;
        }

        //-----------------------------------------------------------------------
        /**
         * The meta-property for the {@code intArray} property.
         * @return the meta-property, not null
         */
        public MetaProperty<int[]> intArray() {
            return intArray;
        }

        /**
         * The meta-property for the {@code longArray} property.
         * @return the meta-property, not null
         */
        public MetaProperty<long[]> longArray() {
            return longArray;
        }

        /**
         * The meta-property for the {@code doubleArray} property.
         * @return the meta-property, not null
         */
        public MetaProperty<double[]> doubleArray() {
            return doubleArray;
        }

        /**
         * The meta-property for the {@code booleanArray} property.
         * @return the meta-property, not null
         */
        public MetaProperty<boolean[]> booleanArray() {
            return booleanArray;
        }

        //-----------------------------------------------------------------------
        @Override
        protected Object propertyGet(Bean bean, String propertyName, boolean quiet) {
            switch (propertyName.hashCode()) {
                case 537167786:  // intArray
                    return ((ImmArrays) bean).getIntArray();
                case 100362557:  // longArray
                    return ((ImmArrays) bean).getLongArray();
                case -1645494008:  // doubleArray
                    return ((ImmArrays) bean).getDoubleArray();
                case -1066176751:  // booleanArray
                    return ((ImmArrays) bean).getBooleanArray();
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
     * The bean-builder for {@code ImmArrays}.
     */
    public static final class Builder extends DirectFieldsBeanBuilder<ImmArrays> {

        private int[] intArray;
        private long[] longArray;
        private double[] doubleArray;
        private boolean[] booleanArray;

        /**
         * Restricted constructor.
         */
        private Builder() {
        }

        /**
         * Restricted copy constructor.
         * @param beanToCopy  the bean to copy from, not null
         */
        private Builder(ImmArrays beanToCopy) {
            this.intArray = (beanToCopy.getIntArray() != null ? beanToCopy.getIntArray().clone() : null);
            this.longArray = (beanToCopy.getLongArray() != null ? beanToCopy.getLongArray().clone() : null);
            this.doubleArray = (beanToCopy.getDoubleArray() != null ? beanToCopy.getDoubleArray().clone() : null);
            this.booleanArray = beanToCopy.getBooleanArray();
        }

        //-----------------------------------------------------------------------
        @Override
        public Object get(String propertyName) {
            switch (propertyName.hashCode()) {
                case 537167786:  // intArray
                    return intArray;
                case 100362557:  // longArray
                    return longArray;
                case -1645494008:  // doubleArray
                    return doubleArray;
                case -1066176751:  // booleanArray
                    return booleanArray;
                default:
                    throw new NoSuchElementException("Unknown property: " + propertyName);
            }
        }

        @Override
        public Builder set(String propertyName, Object newValue) {
            switch (propertyName.hashCode()) {
                case 537167786:  // intArray
                    this.intArray = (int[]) newValue;
                    break;
                case 100362557:  // longArray
                    this.longArray = (long[]) newValue;
                    break;
                case -1645494008:  // doubleArray
                    this.doubleArray = (double[]) newValue;
                    break;
                case -1066176751:  // booleanArray
                    this.booleanArray = (boolean[]) newValue;
                    break;
                default:
                    throw new NoSuchElementException("Unknown property: " + propertyName);
            }
            return this;
        }

        @Override
        public Builder set(MetaProperty<?> property, Object value) {
            super.set(property, value);
            return this;
        }

        @Override
        public ImmArrays build() {
            return new ImmArrays(
                    intArray,
                    longArray,
                    doubleArray,
                    booleanArray);
        }

        //-----------------------------------------------------------------------
        /**
         * Sets the intArray.
         * @param intArray  the new value
         * @return this, for chaining, not null
         */
        public Builder intArray(int... intArray) {
            this.intArray = intArray;
            return this;
        }

        /**
         * Sets the longArray.
         * @param longArray  the new value
         * @return this, for chaining, not null
         */
        public Builder longArray(long... longArray) {
            this.longArray = longArray;
            return this;
        }

        /**
         * Sets the doubleArray.
         * @param doubleArray  the new value
         * @return this, for chaining, not null
         */
        public Builder doubleArray(double... doubleArray) {
            this.doubleArray = doubleArray;
            return this;
        }

        /**
         * Sets the booleanArray.
         * @param booleanArray  the new value
         * @return this, for chaining, not null
         */
        public Builder booleanArray(boolean... booleanArray) {
            this.booleanArray = booleanArray;
            return this;
        }

        //-----------------------------------------------------------------------
        @Override
        public String toString() {
            StringBuilder buf = new StringBuilder(160);
            buf.append("ImmArrays.Builder{");
            buf.append("intArray").append('=').append(JodaBeanUtils.toString(intArray)).append(',').append(' ');
            buf.append("longArray").append('=').append(JodaBeanUtils.toString(longArray)).append(',').append(' ');
            buf.append("doubleArray").append('=').append(JodaBeanUtils.toString(doubleArray)).append(',').append(' ');
            buf.append("booleanArray").append('=').append(JodaBeanUtils.toString(booleanArray));
            buf.append('}');
            return buf.toString();
        }

    }

    //-------------------------- AUTOGENERATED END --------------------------
}
